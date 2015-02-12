---
layout: post
title: "Updates on Snow Lysimeter and Precipitation on UPLMET, CENMET, and H15MET"
date: 2015-02-12T09:03:32-08:00
---

## Overview

In the document [here](http://dataronin.github.io/metQC/2015/02/05/upl-snow-and-pre.html) we found a discrepancy between the amount of snow measured by the snow lysimeter on UPLMET and what we would expect based on the precipitation. 

To update our analysis I:

* quickly ran a reduced version of the precipitation [algorithm](#algorithm) on the final 3 months of 2014 for UPLMET and CENMET (and ran the same algorithm over 2013 on H15MET as validation)

* found times of year in each of the three stations where snow melt apparently happened, despite no snow water equivalence value, and it being "summer".

* graphed the snow-melt from the snow-melt lysimeter, precipitation from both of the two gages, and swe (when available) to visualize where values were not in synchrony.

## Key Points:

The following observations are mentioned in greater detail below:

* Overlap in data on Portal between the 2014 and 2015 arrays initially caused an over-estimation in my calculations. The data between 2014-12-11 and 2014-12-28 are repeated in both the 2014 and 2015 csv files.

* a row of data on Portal from 2014-12-13 on UPLMET may contain important snow and precipitation values but has been turned missing

        "UPLMET_227",2014-12-13 19:25:00,NaN,"M",NaN,"IM",NaN,"M",NaN,"M",47.865,"E",NaN,"",NaN,"M",76.30,"E",NaN,"",NaN,"M",NaN,"M",NaN,"",NaN,"",NaN,"M"

* On CENMET in calendar 2013 prior to the WY 2014, snow lysimeter measurements are unusually low as compared to the other [stations](#lowcen); however, measurements after the water year are more similar to those of the other two stations.

* In calendar 2014, [UPLMET](#highupl) has much higher snow-melt and precipitation prior to the WY 2015 than CENMET does

* in WY 2014, there is ["summertime snow"](#summersno) on UPLMET that does not seem reasonable.

* Two events in 2014 seem to have incresed the total UPLMET precipitation in both rain and snow-- the cold-spell in February 2014 and a December rain and [snow event](#spike).

* the SWE from 

## Details:

### Snow-melt lysimeter and precipitation before and after the water-year for Calendar 2013 and Calendar 2014 on CENMET, UPLMET, and H15MET.

Here's a table of values for 2014 snow on UPLMET and CENMET, before and after the water year:<a id= "highupl"></a>


| Station | Sno < 10-01 | Sno > 10-01 |  Probe | Pre < 10-01 | Pre > 10-01 |
| ----| ---| ---| ---| 
| CENMET | 1665.4 | 1007.2 | lyscen01 | 1673.29 | 1106.61| pptcen01 |
| UPLMET | 2616.6 | 1268.9 | lysupl01 | 2234.59 | 1323.77 | pptupl01 |
| H15MET | 1738.6 | 1020.5 | lysh1501 | NA | NA | NA |


Compare to a table of the snow values for all of 2013, and their corresponding precipitation values (here with stand-alone precipitation gage)<a id="lowcen"></a>


| Station | Sno < 10-01 | Sno > 10-01 |  Probe | Pre < 10-01 | Pre > 10-01 | Probe |
| ----| ---| ---| ---| 
| CENMET | 683.1 | 380.6| lyscen01 | 886.89 | 509.89| pptcen01 |
| UPLMET | 1746.5 | 493.7| lysupl01 | 1244.64 | 582.94 | pptupl01 |
| H15MET | 1505.4 |  388.3 | lysh1501 | 515.06 | 382.92 | ppth1501 |
 

### Summer-time snow lysimeter measurements on UPLMET that seem unreasonable.<a id="summersno"></a>

On UPLMET in 2014, there are some snow patterns that do not seem reasonable.

        date: 2014-06-09 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-06-10 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-06-11 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-06-12 00:00:00, rain: 0.0, sno: 5.3, swe: 0.0
        date: 2014-06-13 00:00:00, rain: 0.0, sno: 22.6, swe: 0.0
        date: 2014-06-14 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-06-15 00:00:00, rain: 0.0, sno: 1.0, swe: 0.0
        date: 2014-06-16 00:00:00, rain: 0.0, sno: 22.4, swe: 0.0
        date: 2014-06-17 00:00:00, rain: 0.0, sno: 6.5, swe: 0.0

        date: 2014-08-28 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-08-29 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-08-30 00:00:00, rain: 0.0, sno: 13.4, swe: 0.0
        date: 2014-08-31 00:00:00, rain: 0.0, sno: 0.3, swe: 0.0
        date: 2014-09-01 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0
        date: 2014-09-02 00:00:00, rain: 0.0, sno: 0.0, swe: 0.0


### Cold february in 2014 that may affect UPLMET snow and precipitation:

        date: 2014-02-10 00:00:00, rain: 13.1, sno: 23.3, swe: 314.8
        date: 2014-02-11 00:00:00, rain: 22.8, sno: 16.6, swe: 321.0
        date: 2014-02-12 00:00:00, rain: 112.1, sno: 204.5, swe: 337.7
        date: 2014-02-13 00:00:00, rain: 11.01, sno: 32.0, swe: 320.3
        date: 2014-02-14 00:00:00, rain: 81.12, sno: 100.8, swe: 280.3
        date: 2014-02-15 00:00:00, rain: 32.1, sno: 47.0, swe: 251.6
        date: 2014-02-16 00:00:00, rain: 18.9, sno: 0.8, swe: 228.8

### Spike in December Precipitation and Snow on UPLMET, 2014 <a id="spike"></a>

<iframe src="http://bl.ocks.org/dataRonin/raw/5db9e0cd181a8274a6b2/f3cf672c0b57b76453a4461a0e8fa10889e9a924/"  width="600" height = "500" scrolling="yes"></iframe><br>
<p><aside><a style="position:relative;top:6px;" href="/dataRonin/raw/5db9e0cd181a8274a6b2/" target="_blank">Open in a new window.</a></aside></p>


### UPLMET in 2014 Precipitation (blue), Snow(orange), and SWE(crimson) - only available for part of the year

<iframe src="http://bl.ocks.org/dataRonin/raw/3449fc37f4b2ab618a80/18166936651db80af137838bd07cbb25d66aecf8/"  width="600" height = "500" scrolling="yes"></iframe><br>
<p><aside><a style="position:relative;top:6px;" href="/dataRonin/raw/3449fc37f4b2ab618a80/" target="_blank">Open in a new window.</a></aside></p>


### CENMET in 2014 Precipitation (blue), Snow(orange), and SWE(crimson) - only available for part of the year

<iframe src="http://bl.ocks.org/dataRonin/raw/c1d0dcacf33f021941f0/8f09350774d4a085d0a8f2485d8a509f26018d8c/"  width="600" height = "500" scrolling="yes"></iframe><br>
<p><aside><a style="position:relative;top:6px;" href="/dataRonin/raw/c1d0dcacf33f021941f0/" target="_blank">Open in a new window.</a></aside></p>


## Algorithm <a id="algorithm"></a>

This is a shorter version of the precipitation algorithm designed to quickly get precipitation. It does not include a "summer mode" as we use in the original algorithm for not including very small gains in precipitation, nor is it as careful about detecting bounce-backs after resets (it will allow any inputs up to 5 mm). As such, it would be expected to slightly over-predict precipitation in any given circumstance.


        def gen_seq():
            
            with open("h15pre.csv","rb") as readfile:
                reader = csv.reader(readfile)

                whichrow = 0.
                last_reading = 0.
                accumulation = 0.

                od = {}

                for row in reader:

                    # change to row 2 for h15
                    dt = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')

                    # if it's the start of a new water year
                    if dt.month == 10 and dt.day == 01 and dt.hour == 0 and dt.minute == 0.:
                        accumulation =0.
                    else:
                        pass

                    # change to row 16 for sh - upl
                    # change to row 9 for sa - cen
                    # change to row 15 for sh -cen
                    the_gage = float(row[9])

                    diff_gage = the_gage - last_reading

                    if diff_gage >= 0. and diff_gage < 5.:
                        # new value is 201, old value is 200, set old value to 201, add 1 to acc
                        last_reading = the_gage
                        accumulation += diff_gage

                    elif diff_gage < -5.:
                        # new value is 30, old value was 200, set new value to 30, do not acc
                        last_reading = the_gage

                    elif diff_gage < 0. and diff_gage >=-5.:
                        # new value is 199, old value was 200, do not reset value, do not acc
                        pass

                    elif diff_gage >= 5.:
                        # new value is 205, old value was 200, do not reset value, do not acc
                        pass

                    else:
                        diff_gage = 0.
                        last_reading = the_gage


                    if dt.year not in od:
                        od[dt.year] = {dt.month: {dt.day: [[dt.hour, dt.minute, last_reading, accumulation]]}}
                    elif dt.year in od:
                        if dt.month not in od[dt.year]:
                            od[dt.year][dt.month] = {dt.day:[[dt.hour, dt.minute, last_reading, accumulation]]}
                        elif dt.month in od[dt.year]:
                            if dt.day not in od[dt.year][dt.month]:
                                od[dt.year][dt.month][dt.day] = []
                                od[dt.year][dt.month][dt.day].append([dt.hour, dt.minute, last_reading, accumulation])
                            else:
                                od[dt.year][dt.month][dt.day].append([dt.hour, dt.minute, last_reading, accumulation])

                    #print "dt: %s%s%s%s%s, accumulation: %s, baseline %s" %(dt.year, dt.month, dt.day, dt.hour, dt.minute, accumulation, last_reading)
                    
                    try:
                        whichrow += 1
                    except Exception:
                        return accumulation, od

            return od