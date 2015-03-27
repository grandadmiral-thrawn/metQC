---
layout: post
title: "Sarah's Reference Stands Temperature Merger"
date: 2015-03-27T16:33:04-07:00
---

For research on bird plots and phenology we needed to append to an old, merged data set some "newer" temperature data from our reference stands. The formating of the old data was particularly problematic in this case because it was not very similar to what we accept for our databank. Nonetheless, it was not terrible to create a merger script. The main issue is that this data is opened and manipulated in EXCEL, which uses a type of encoding that Python strongly dislikes. I was able to come up with a method to circumvent this by dealing directly with string manipulations, very pythonic.  Here's code to use to do this merger. Note that the portion of this code for extracting the benchmark stations IS NOT COMPLETE, as I need to do a little reformating on the dates to make sure I put using csv's not-controlled, not-flagged code as a better priority than our quality-controlled code from the database. This is a logic I don't normally use, so it's a neat challenge to over-ride my assumptions.

        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        import numpy as np
        import datetime
        import csv
        import datetime
        import decimal
        import math
        import itertools
        import pymssql
        from rescue_ref import form_connection

        def get_fsdb_data_rs(stand):
            ''' get from january 1, 2009 at midnight to may 1 2009 at midnight (start of day)
            from fsdb from ms005'''

            # database connection
            c = form_connection()
            # create empty strings for time and temperature
            time = []
            temp = []

            query1 = "SELECT DATE_TIME, MEANTEMP \
            FROM FSDBDATA.DBO.MS00511 \
            WHERE SITECODE LIKE \'" + stand + "%\' \
            AND DATE_TIME > '2008-12-31 23:00' \
            AND DATE_TIME < '2009-05-01 01:00' \
            ORDER BY DATE_TIME ASC"

            c.execute(query1)

            for row in c:
                dt = datetime.datetime.strftime(row[0],'%m/%d/%Y %H:%M')
                value = str(row[1])

                time.append(dt)
                temp.append(value[:5])

            return time, temp


        def import_sarah_data(stand, old_time, old_temp):
            ''' read in sarah's csv file, append it to what you got from fsdb'''
            
            sarah = {'RS02':'Ref_RS02_2009_2013_reformatted.csv',
            'RS04':'Ref_RS04_2009_2013_reformatted.csv',
            'RS05':'Ref_RS05_2009_2013_reformatted.csv',
            'RS10':'Ref_RS10_2009_2013_reformatted.csv',
            'RS12':'Ref_RS12_2009_2013_reformatted.csv',
            'RS20':'Ref_RS20_2009_2013_reformatted.csv',
            'RS26':'Ref_RS26_2009_2013_reformatted.csv',
            'RS86':'Ref_RS86_2009_2013_reformatted.csv',
            'RS38':'Ref_TS38_2009_2013_reformatted.csv',
            'RS89':'Ref_RS89_2009_2013_reformatted.csv',
            'CENMET':'Ref_CENMET4_2009_2013_reformatted.csv',
            'CS2MET':'Ref_RS02_2009_2014_reformatted.csv'}

            sarahfile = sarah[stand]

            with open(sarahfile,'rb') as readfile:
                # removes encoding but keeps new lines
                reader = csv.reader(open(sarahfile, 'rU'), dialect=csv.excel_tab)

                for row in reader:

                    # horrible time formatting conventions due to putting it into EXCEL, must use string magic!
                    # split on comma char
                    temporary = row[0].split(',')

                    # before comma is date, split on slash
                    bad_date = temporary[0].split('/')

                    # the time part is in the 3rd through end columns of the final split (yy TIME.....)
                    bad_time = datetime.datetime.strptime(bad_date[2][3:],'%H:%M')

                    # use the safe time module to cat '20' to the beginning of the year so we don't get a time delta error. Then re-make the date time as a safe time object
                    time1 = datetime.datetime(int('20' +bad_date[2][:2]), int(bad_date[0]), int(bad_date[1]), bad_time.hour, bad_time.minute)

                    # for your viewing pleasure!
                    print time1
                    
                    # temp1 is the temperature (wasn't sure if all the above might cause scope problems)
                    temp1 = str(temporary[1])

                    # if you are on the header, continue
                    if time1 == "time":
                        continue

                    # if the time is greater than the max time of the dataset, continue (to next function)
                    elif time1 > datetime.datetime(2013,12,31,23,0):
                        print "fail"
                        continue

                    # if the time is less than the start, print fail, continue to the next funciton (to get out of the function safely)
                    elif time1 < datetime.datetime(2009,5,1,1,0):
                        print "fail"
                        continue
                    
                    else:

                        # otherwise, append the data to the existing array
                        old_time.append(datetime.datetime.strftime(time1, '%m/%d/%Y %H:%M'))
                        old_temp.append(temp1)

                return old_time, old_temp


        def metdat_fox_data(stand, old_time, old_temp):
            ''' get the metdat salvaged data from metdat, simple '''
            
            # get the data
            c = form_connection()

            # a query for the stand
            query1 = "SELECT TmStamp, AIR_TEMP_AVG from metdat.dbo." + stand + "_115 WHERE TmStamp > \'2013-12-31 23:00\' \
                and TmStamp < '2014-08-01' ORDER by TmStamp asc"
            
            c.execute(query1)

            for row in c:
                dt = datetime.datetime.strptime(str(row[0]).rstrip('0').rstrip('.'), '%Y-%m-%d %H:%M:%S')
                time = datetime.datetime.strftime(dt,'%m/%d/%Y %H:%M')
                temp = str(row[1])[:5]

                old_time.append(time)
                old_temp.append(temp)

            return old_time, old_temp
            

        def export_sarah_data(stand, old_time, old_temp):
            ''' write out sarah and sherris files'''

            filename = "Ref_" + stand + "_2009_2014_reformatted.csv"
            filename2 = "Ref_" + stand + "_jan2009_2014_reformatted.csv"
            with open(filename2,'wb') as writefile, open(filename, 'wb') as sarahfile:
                writer = csv.writer(writefile, quoting = csv.QUOTE_NONNUMERIC, delimiter = ",")
                writer.writerow(["time","temp"])

                writer_sarah = csv.writer(sarahfile, quoting = csv.QUOTE_NONNUMERIC, delimiter = ",")
                writer_sarah.writerow(["time","temp"])

                new_time = [timex for timex in old_time if datetime.datetime.strptime(timex,'%m/%d/%Y %H:%M') > datetime.datetime(2009,5,1,0,0)]

                new_temp = [y for i,y in enumerate(old_temp) if datetime.datetime.strptime(old_time[i],'%m/%d/%Y %H:%M') > datetime.datetime(2009,5,1,0,0)]
                
                for (x,y) in itertools.izip(old_time, old_temp):
                    writer.writerow([x,y])

                for(shortx, shorty) in itertools.izip(new_time, new_temp):
                    writer_sarah.writerow([shortx, shorty])
            

        if __name__ == "__main__":
            ''' 
            iterate over the files, generating both results.'''

            for stand_name in ['RS02', 'RS04','RS05','RS10','RS12','RS20','RS26','RS86','RS89','RS38']:
            
                complete_time, complete_temp = get_fsdb_data_rs(stand_name)

                complete_time, complete_temp = import_sarah_data(stand_name,complete_time, complete_temp)

                complete_time, complete_temp = metdat_fox_data(stand_name,complete_time, complete_temp)

                export_sarah_data(stand_name,complete_time, complete_temp)

                print "processed %s ..." %stand_name

                # clear out your variables/lists!
                del complete_time, complete_temp, stand_name