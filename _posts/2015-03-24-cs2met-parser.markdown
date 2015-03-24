---
layout: post
title: "Cs2met Parser"
date: 2015-03-24T14:02:41-07:00
---


The following is a set of two functions that can be used to parse the DAT files from CS2met. 
In the future this script could run on any list of CS2met DAT files, and it would parse and concatenate them together. 

This function does not flag or gap fill. However, it does calculate dewpoint, satvp, and VPD

        import datetime
        import csv
        import math

        def cs2parse(probe_index, attribute):
            ''' 
            A function to take the .dat files from cs2met clim logger an convert them into meaningful arrays
            for xtempx program. Makes 3 data arrays, hourly, fifteen, and daily, and three flag arrays containing default
            flags of 'N' for each attribute because they are Not on Portal.

            probe_index is an integer, like 1, 2, or 4, which represents the probe number
            attribute is the thing being calculated, such as airtemp or relhum

            To add or change files in the same format append to the subsequent list. It doesn't matter the order, as dictionaries are unordered.
            Sort the dictionaries in xtempx or map them to other files as you nee.
            '''

            # inputs: 
            files = ['CLIM_2014.DAT','CLIM_2015_013.DAT','CLIM_2015_034.DAT', 'CLIM_2015_055.DAT']

            # data dictionaries:
            hourly = {}
            fifteen = {}
            daily = {}

            # flag dictionaries:
            hf = {}
            ff = {}
            df = {}

            # iterate over files
            for each_file in files:

                # read each file
                with open(each_file, 'rb') as f:
                    
                    while True:

                        a = f.readline()
                        line_items = a.strip('\r\n').split(',')
                        
                        try:
                            year = int(line_items[2])
                        except IndexError:
                            print "that was the last index possible"
                            break

                        # extract doy, hhmm
                        doy = int(line_items[3])
                        hhmm = int(line_items[4])
                        
                        if len(str(hhmm)) == 4:
                            hh = int(str(hhmm)[0:2])
                            mm = int(str(hhmm)[-2:])

                        elif len(str(hhmm)) ==3:
                            hh = int(str(hhmm)[0:1])
                            mm = int(str(hhmm)[-2:])

                        elif len(str(hhmm)) <=2:
                            hh = 0
                            mm = hhmm

                        else: 
                            pass

                        # extract temperature
                        temp = str(line_items[5])

                        # use the dtmod function here to convert the date time to human
                        converted = dtmod(year, doy, hh, mm, hhmm)
                        
                        # the fifteen minute record is array 115
                        if str(line_items[0]) == "115":
                            fifteen[converted] = temp
                            ff[converted] = ""
                        
                        # the hourly record is array 110
                        elif str(line_items[0]) == "110":
                            if attribute == "relhum":
                                hourly[converted] = str(line_items[5])
                                hf[converted] = ""
                            
                            elif attribute == "airtemp":

                                hourly[converted] = str(line_items[6])
                                hf[converted] = ""

                            # if we can calculate the dewpoint, do so using the dewpoint calculations included in here
                            elif attribute == "dewpt":
                                svp = satvp(line_items[6])
                                dp = dewpt(svp, line_items[5])
                                hourly[converted] = str(dp)
                                hf[converted] = "Mc"

                            # if we can calculate the vpd, do so using the vpd calculations included in here
                            elif attribute == "vpd":
                                svp = satvp(line_items[6])
                                vp = vaporpresd(line_items[5], svp)
                                hourly[converted] = str(vp)
                                hf[converted] = "Mc"
                            else:
                                pass

                        # the daily data is in array 105
                        elif str(line_items[0]) == "105":

                            # map the raw data to the time stamp, an assign a flag of "" (can be flagged in xtempx)
                            if attribute == "airtemp":
                                daily[converted] = str(line_items[5])
                                df[converted]= ""
                            elif attribute == "relhum":
                                daily[converted] = str(line_items[6])
                                df[converted]= ""
                            elif attribute == "dewpt":
                                daily[converted] = str(line_items[7])
                                df[converted] =""
                            elif attribute == "vpd":
                                daily[converted] = str(line_items[8])
                                df[converted] =""
                            
                            # similar to the raw data, match the max, min, maxtime, and mintime and assign a flag of ""
                            elif attribute == "airtemp_max":
                                daily[converted] = str(line_items[9])
                                df[converted]= ""
                            elif attribute == "airtemp_maxtime":
                                daily[converted] = str(line_items[10])
                                df[converted]= ""
                            elif attribute == "relhum_max":
                                daily[converted] = str(line_items[11])
                                df[converted]= ""
                            elif attribute == "relhum_maxtime":
                                daily[converted] = str(line_items[12])
                                df[converted]= ""
                            elif attribute == "dewpt_max":
                                daily[converted] = str(line_items[13])
                                df[converted] =""
                            elif attribute == "dewpt_maxtime":
                                daily[converted] = str(line_items[14])
                                df[converted] =""
                            elif attribute == "vpd_max":
                                daily[converted] = str(line_items[15])
                                df[converted] =""
                            elif attribute == "vpd_maxtime":
                                daily[converted] = str(line_items[16])
                                df[converted] =""

                            elif attribute == "airtemp_min":
                                daily[converted] = str(line_items[17])
                                df[converted]= ""
                            elif attribute == "airtemp_mintime":
                                daily[converted] = str(line_items[18])
                                df[converted]= ""
                            elif attribute == "relhum_min":
                                daily[converted] = str(line_items[19])
                                df[converted]= ""
                            elif attribute == "relhum_mintime":
                                daily[converted] = str(line_items[20])
                                df[converted]= ""
                            elif attribute == "dewpt_min":
                                daily[converted] = str(line_items[21])
                                df[converted] =""
                            elif attribute == "dewpt_mintime":
                                daily[converted] = str(line_items[22])
                                df[converted] =""
                            elif attribute == "vpd_min":
                                daily[converted] = str(line_items[23])
                                df[converted] =""
                            elif attribute == "vpd_mintime":
                                daily[converted] = str(line_items[24])
                                df[converted] =""
                        else:
                            pass

            # returns maps for hourly, hourly flags, fifteen minute, fifteen minute flags, daily, and daily flags (datetime: value or datetime:flag)
            return hourly, hf, fifteen, ff, daily, df

        def dtmod(year, doy, hh, mm, hhmm):
                """ converts ymd to jday"""
                dt1 = datetime.datetime(year, 1, 1) + datetime.timedelta(int(doy) - 1) + datetime.timedelta(hours=int(hh)) + datetime.timedelta(minutes = int(mm))
                
                # year end convention needs to be worked with
                if doy == 365 and hhmm == 2400:
                    dt1 = datetime.datetime(year + 1, 1, 1, 0, 0)
                else:
                    pass

                return dt1                   


        def satvp(Ta):
            SatVP = 6.1094*math.exp((17.625*float(Ta))/(243.04+float(Ta)))
            return SatVP

        def regular_vp(Td):
            regvap = 6.1094*math.exp((17.625*float(Td))/(243.04+float(Td)))
            return regvap

        def dewpt(SatVP, RH):
            try:
                Td = 237.3*math.log(SatVP*float(RH)/611.)/(7.5*math.log(10)-math.log(SatVP*float(RH)/float(611.)))
                return Td
            except Exception:
                Td = None
                return Td

        def relhum(vap,SatVP):
            RH = regvap/SatVP
            return RH

        def vaporpresd(RH, SatVP):
            try:
                vpd = ((100-RH)*0.01)*float(SatVP)
                #vap = float(RH)*0.01*float(SatVP)
                return vpd
            except Exception:
                vpd = None
        return vpd

if __name__ == "__main__":

    a,b,c,d,e,f = cs2parse(1,"airtemp")

