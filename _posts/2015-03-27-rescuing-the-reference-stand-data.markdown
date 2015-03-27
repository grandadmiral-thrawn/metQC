---
layout: post
title: "Rescuing the Reference Stand Data"
date: 2015-03-27T10:38:38-07:00
---

Although it was our intention to have all of the air temperatures up to date, we noticed that the air temperatures and soil temperatures for the reference stands had not been updated since 2011 (and were needed by some students). Portal did not have an updated version, either; although data was present it was of low-quality, without flags and range checks. We quickly wrote up a solution for gathering the old reference stand data from the METDAT database. During the process, we went ahead and gathered the new five-minute data as well, for both air and soil.

I noticed that the stop time for the old sensors is 2015-01-01 (ish) and the start time for the old sensors is not before 2014-05-10 (ish). To produce some overlap, I ran the hourly data separate from the five minute data, which is helpful for the student who needs it. We had generally decided to start the new data in that May when the five-minute method starts, so the simplest solution will to be simply cut the old data for each stand (hence why they are all in separate files) to the appropriate stop date (23:00 on 2014-05-09) and begin the new data on 00:00 2014-05-10.  I will perform this append once the data has been QC'ed  by Don. 

There are two bound sets for this data which are not the traditional airbounds.yaml. These are airbounds_rs.yaml and soilbounds_rs.yaml. These bounds are four sigma bounds specific to the reference stands. They are more constrained than the others. 


The section below is code for getting the reference stand data (hourly and five minutes). The write string for the hourly has been removed as I was working with the five minute data, but it would be simple to add back in:

        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        import numpy as np
        import datetime
        import csv
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import mpld3
        import datetime
        import decimal
        import math
        import yaml
        import pymssql



        def form_connection():
            """
            connects to the METDAT database to gather the data
            returns a cursor
            """

            # Connect to MSSQL Server
            conn = pymssql.connect(server="",
                                   user="",
                                   password="",
                                   database="")

            # Create a database cursor
            cursor = conn.cursor()

            return cursor

        def load_bounds():
            ''' loads the bounds from the yaml file if needed for a four sigma test -- air temperature'''
            
            bounds = yaml.load(open('airbounds_rs.yaml','r'))
            
            return bounds

        def load_sbounds():
            ''' loads the bounds from the yaml file if needed for a four sigma test -- soil temperature'''
            
            sbounds = yaml.load(open('soilbounds_rs.yaml','r'))
            
            return sbounds


        def read_hrly_at(stand, cursor, bounds):
            ''' 
            reads the atmospheric pressure from metdat and generates 
            FSDB-style output
            '''
            
            # a dictionary for air temperature (atd) and one for flags (afd)
            atd = {}
            atfd = {}

            # a query for the stand, in hourly data
            query1 = "SELECT TmStamp, AIR_TEMP_AVG from metdat.dbo." + stand + "_115 WHERE TmStamp > \'2010-12-31\' ORDER by TmStamp asc"
            
            # execute query
            cursor.execute(query1)
            
            # iterate over the cursor, getting dates and doing flagging
            for row in cursor:
               
                
                # get date times
                dt = datetime.datetime.strptime(str(row[0]).rstrip('0').rstrip('.'), '%Y-%m-%d %H:%M:%S')
                # get values
                at = str(row[1])

                try:
                    # make the date time so it can be checked against the bounds
                    dt_b = datetime.datetime(2014, dt.month, dt.day, dt.hour, 0)
                except ValueError:
                    # leap year
                    dt_b = datetime.datetime(2014, dt.month, 28, dt.hour, 0)



                # if no value, missing
                if at == "None":
                    atf = "M"
                
                # if not missing, check is in bounds, if not "Q"
                elif float(at) < -30. or float(at) > 50.  :
                    atf = "M"

                # is in bounds of the four sigma?
                elif float(at) < bounds[dt_b]['lo'] or float(at) > bounds[dt_b]['hi']:
                    atf = "Q"

                # is in bounds of the Questionable?
                elif float(at) < -20. or float(at) > 45.:
                    atf = "Q"

                # if behaves well, "A"
                else:
                    atf = "A"

                # add to output - if the date is not in the dictionary
                if dt not in atd:
                    # add it
                    atd[dt] = at
                # but if it is there
                elif dt in atd:
                    # print that it is duplicated
                    print "duplicate entry: %s: %s" %(dt, at)

                # if the date time is not in the flags
                if dt not in atfd:
                    # add it
                    atfd[dt] = atf
                # but if it is in the flags
                elif dt in atfd:
                    # print that it is already there
                    print "duplicate entry: %s: %s" %(dt, atfd)

            return atd, atfd

        def read_highres_at(stand, cursor, bounds, sbounds):
            ''' Get the high resolution air temperature and soil temperature when you can- start may 10, 2014'''
            
            # load air bounds and soil bounds
            #bounds = load_bounds()
            #sbounds = load_sbounds()

            # temperature dictionary
            td = {}

            # temperature flags dictionary
            tfd ={}

            # a look up for the stands we have at 5 minute right now
            sd = {'RS04':'RS04_91_Table105',
                'RS12': 'RS12_94_Table105',
                'RS20': 'RS20_95_Table105',
                'RS26': 'RS26_96_Table105',}

            # construct and execute query, also get soil T
            query1 = "SELECT TmStamp, AIR_02_Avg, AIR_03_Avg, SoilT_10_AVG, SOILT_20_AVG, SOILT_30_AVG, BATT_Avg from metdat.dbo." + sd[stand] + " WHERE TmStamp >= \'2014-05-10\' ORDER by TmStamp asc"

            cursor.execute(query1)

            # iterate over the cursor, getting dates and doing flagging
            for row in cursor:
                
                # get date times
                dt = datetime.datetime.strptime(str(row[0]).rstrip('0').rstrip('.'), '%Y-%m-%d %H:%M:%S')
                
                # get values
                t2 = str(row[1])
                t3 = str(row[2])
                s1 = str(row[3])
                s2 = str(row[4])
                s3 = str(row[5])
                b = str(row[6])

                try:
                    # make the date time so it can be checked against the bounds
                    dt_b = datetime.datetime(2014, dt.month, dt.day, dt.hour, 0)
                
                except ValueError:
                    
                    # leap year
                    dt_b = datetime.datetime(2014, dt.month, 28, dt.hour, 0)

                # if no value, missing -- or if value just very crazy, missing
                if t2 == "None" or float(t2) < -30. or float(t2) > 50. or float(b) < 0.:
                    t2f = "M"
                # is in bounds of the four sigma?
                elif float(t2) < bounds[dt_b]['lo'] or float(t2) > bounds[dt_b]['hi'] or float(t2) < -20. or float(t2) > 45.:
                    t2f = "Q"
                else:
                    t2f = "A"

                # if no value, missing -- or if value just very crazy, missing
                if t3 == "None" or float(t3) < -30. or float(t3) > 50. or float(b) < 0.:
                    t3f = "M"
                # is in bounds of the four sigma?
                elif float(t3) < bounds[dt_b]['lo'] or float(t3) > bounds[dt_b]['hi'] or float(t3) < -20. or float(t3) > 45.:
                    t3f = "Q"
                else:
                    t3f = "A"

                # if no value, missing -- or if value just very crazy, missing
                if s1 == "None" or float(s1) < -10. or float(s1) > 35. or float(b) < 0.:
                    s1f = "M"
                # is in bounds of the four sigma?
                elif float(s1) < bounds[dt_b]['lo'] or float(s1) > bounds[dt_b]['hi'] or float(s1) < -5. or float(s1) > 30.:
                    s1f = "Q"
                else:
                    s1f = "A"

                # if no value, missing -- or if value just very crazy, missing
                if s2 == "None" or float(s2) < -10. or float(s2) > 35. or float(b) < 0.:
                    s2f = "M"
                # is in bounds of the four sigma?
                elif float(s2) < bounds[dt_b]['lo'] or float(s2) > bounds[dt_b]['hi'] or float(s2) < -5. or float(s2) > 30.:
                    s2f = "Q"
                else:
                    s2f = "A"

                # if no value, missing -- or if value just very crazy, missing
                if s3 == "None" or float(s3) < -10. or float(s3) > 35. or float(b) < 0.:
                    s3f = "M"
                # is in bounds of the four sigma?
                elif float(s3) < bounds[dt_b]['lo'] or float(s3) > bounds[dt_b]['hi'] or float(s3) < -5. or float(s3) > 30.:
                    s3f = "Q"
                else:
                    s3f = "A"

                # is the battery terrible? -- give a "B" for now, and later do an event code
                if float(b) < 12. and float(b) > 0.:
                    
                    t2f = 'B'
                    t3f = 'B'
                    s1f = 'B'
                    s2f = 'B'
                    s3f = 'B'
                
                elif float(b) > 16.:

                    t2f = 'B'
                    t3f = 'B'
                    s1f = 'B'
                    s2f = 'B'
                    s3f = 'B'
                
                else:
                    pass

                
                # add to output - if the date is not in the dictionary
                if dt not in td:
                    # add it
                    td[dt] = {'at2': t2, 'at3': t3, 'st1': s1, 'st2':s2, 'st3': s3}
                # but if it is there
                elif dt in td:
                    # print that it is duplicated
                    print "duplicate entry: %s: %s, %s, %s, %s, %s" %(dt, t2, t3, s1, s2, s3)

                # if the date time is not in the flags
                if dt not in tfd:
                    # add it
                    tfd[dt] = {'at2': t2f, 'at3': t3f, 'st1': s1f, 'st2':s2f, 'st3': s3f}
                # but if it is in the flags
                elif dt in tfd:
                    # print that it is already there
                    print "duplicate entry: %s: %s, %s, %s, %s, %s" %(dt, t2f, t3f, s1f, s2f, s3f)

            return td, tfd

        def drange(start, stop, step):
                """ define an interval range over which to iterate
                final arguement can let you iterate with a jump
                that is not 1 (i.e. 10 or 0.4)

                for example:
                thisrange = drange(0.0, 250.0, 0.1)
                here's how to see the whole range
                ranger = [round(x,2) for x in thisrange]

                THIS IS GOD'S FUNCTION.
                """

                r = start
                while r < stop:
                    yield r
                    r+=step

        def fill_gaps_in_dt(attribute, isflag):
            ''' each data set may be missing some dates - fill in from an ideal series '''
            
            gapfiller = drange(datetime.datetime(2010,12,31,0,0), datetime.datetime(2015,01,01,0,0), datetime.timedelta(minutes=60))
            
            # the intersection of the perfect date range and the real date range
            remaining = list(set([x for x in gapfiller]) -set(attribute.keys()))
                
            # if any dates are missing, fill them in with the appropriate date. 
            if remaining != []:

                # if the column is not a flag column, put in "none" for missing values
                if isflag == "F":
                    attribute.update({remaining[x]:"None" for x,_ in enumerate(remaining)})

                # if the column is a flag column put in "M" for the missing data
                elif isflag == "T":
                    attribute.update({remaining[x]:"M" for x,_ in enumerate(remaining)})
            
            # if nothing is missing, pass
            else:
                pass

            return attribute

        def fill_gaps_in_dt_5(attribute, isflag):
            ''' each data set may be missing some dates - 5 minute filler, made differently here because all the dictionary entries for each temp and soil were in one layer to save space '''
            
            gapfiller = drange(datetime.datetime(2014,5,10,0,0), datetime.datetime(2015,01,01,0,0), datetime.timedelta(minutes=5))
            
            # the intersection of the perfect date range and the real date range
            remaining = list(set([x for x in gapfiller]) -set(attribute.keys()))
                
            if remaining != []:

                # import pdb; pdb.set_trace() <-- was using this to debug. Keeping in here in case you use this in the future and want a nice debugger, this is how you get one!

                # if the column is not a flag column, put in "none" for missing values
                if isflag == "F":
                    for x,_ in enumerate(remaining):
                        attribute.update({remaining[x]:{'at2':'None', 'at3': 'None','st1': 'None', 'st2': 'None','st3': 'None'}})

                # if the column is a flag column put in "M" for the missing data
                elif isflag == "T":
                    for x,_ in enumerate(remaining):
                        attribute.update({remaining[x]:{'at2':"M", 'at3': "M",'st1': "M", 'st2': 'M','st3': 'M'}})


            else:
                pass

            return attribute
                
        if __name__ == "__main__":
            ''' central processing loop-- now with normalization!'''
            
            c = form_connection()

            # bounds loaded from yaml file for flagging
            bounds = load_bounds()
            sbounds = load_sbounds()

            #for stand in ['RS02','RS04','RS05','RS10','RS12','RS20','RS26','RS38','RS86','RS89']:
            
            #    hourly_temps, hourly_flags = read_hrly_at(stand, c, bounds)

            for stand in ['RS04','RS12','RS20','RS26']:
                
                five_min_temps, five_min_flags = read_highres_at(stand,c, bounds, sbounds)

                
            #    ori_file = stand + "_hourly.csv"
                filename = stand + "_5minute.csv"
                filename2 = stand + "_soil_5minute.csv"    
                with open(filename,'wb') as writefile, open(filename2, 'wb') as writefile2:
            #   with open(ori_file,'wb') as writefile3:
                    writer = csv.writer(writefile, quoting = csv.QUOTE_NONNUMERIC, delimiter = ",")
                    writer2 = csv.writer(writefile2, quoting = csv.QUOTE_NONNUMERIC, delimiter = ",")
                #   writer3 = csv.writer(writefile3, quoting = csv.QUOTE_NONNUMERIC, delimiter = ",")
                    
                    headers = ["dbcode","entity","sitecode","airtemp_method","height","qclevel",
                    "probe_code","date_time","airtemp_mean","airtemp_flag","event_code"]

                   # writer3.writerow(headers)
                    writer.writerow(headers)

                    headers2 = ["dbcode","entity","sitecode","soiltemp_method","height","qclevel",
                    "probe_code","date_time","soiltemp_mean","soiltemp_flag","event_code"]
                    writer2.writerow(headers2)
                    
                    five_temps_filled = fill_gaps_in_dt_5(five_min_temps, "F")
                    five_flags_filled = fill_gaps_in_dt_5(five_min_flags,"T")

                    #hourly_temps_filled = fill_gaps_in_dt(hourly_temps, "F")
                    #hourly_flags_filled = fill_gaps_in_dt(hourly_flags, "T")

                    # if stand != 'RS20':
                    #     height = 100
                    # else:
                    #     height = 200

                    # event_code = "NA"

                    # for each_date in sorted(hourly_flags_filled.keys()):

                    #     newrow = ["MS043", "50", stand,"AIR060",height, "1D", "AIR" + stand +"260",
                    #     datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), hourly_temps_filled[each_date]['at2'][:7],
                    #     hourly_flags_filled[each_date][:7], event_code]

                    
                    for each_date in sorted(five_flags_filled.keys()):
                        ''' iterate over 5 minute flags'''

                        if flags_filled[each_date]['at2'] != "B":
                            event_code = "NA"
                        else:
                            event_code = "QUALTY"

                        newrow = ["MS043", "50", stand,"AIR025",height, "1D", stand +"005",
                        datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), five_temps_filled[each_date]['at2'][:7],
                        five_flags_filled[each_date]['at2'][:7], event_code]

                        newrow5 = ["MS043", "50", stand,"AIR035",height, "1D", stand +"005",
                        datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), five_temps_filled[each_date]['at3'][:7],
                        five_flags_filled[each_date]['at3'][:7], event_code]

                        writer.writerow(newrow)
                        writer.writerow(newrow5)

                        newrow2 = ["MS043", "51", stand,"SOIL005", 10, "1D", stand +"105",
                        datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), five_temps_filled[each_date]['st1'][:7],
                        five_flags_filled[each_date]['st1'][:7], event_code]

                        newrow3 = ["MS043", "51", stand,"SOIL005", 20, "1D", stand +"205",
                        datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), five_temps_filled[each_date]['st2'][:7],
                        five_flags_filled[each_date]['st2'][:7], event_code]
                        
                        newrow4 = ["MS043", "51", stand,"SOIL005", 30, "1D", stand +"305",
                        datetime.datetime.strftime(each_date, '%Y-%m-%d %H:%M:%S'), five_temps_filled[each_date]['st3'][:7],
                        five_flags_filled[each_date]['st3'][:7], event_code]

                        writer2.writerow(newrow2)

                        writer2.writerow(newrow3)

                        writer2.writerow(newrow4)

