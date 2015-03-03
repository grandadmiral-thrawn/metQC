---
layout: post
title: "Strange Varamet Pattern"
date: 2015-02-08T16:13:59-08:00
---

## A strange pattern that appears with the Date Stamps sometimes. 

This is an informal description of a pattern seen sometimes; I am not sure what it means, but I think it might have to do with when the loggers are being repaired or changed.  Here's an example, on this csv: 

[VARAMET_301_2014](http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VARA/data/varmet_301_a_5min_2014.csv) where the 7:40 value is actually 07:39:59 

        "VARMET",2014-09-2107:25:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:30:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:35:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:39:59,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:44:59,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:49:59,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 07:54:59,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"

        
This is preceded, though, by a fairly lengthy amount of NaN values, which appear to be that the logger is not getting any data, because even if I look at the surrounding hours, I get 0 rows returned in METDAT. 
    
        select * from metdat.dbo.VARA_301_105 where TmStamp > '2014-09-21 06:00:00' and TmStamp < '2014-09-21 09:00:00'

        TmStamp RecNum  LOGGERID    PROGID  Year_RTM    Day_RTM Hour_Minute_RTMPRECIP   OR_TEMP SNOWDEPTH   QUALITY SWE_AVG

What's odd here is the lack of consistency; I see pattern of having the date-value get 'off' by one second in the Portal and the data disappearing in METDAT synchonously somtimes, so I originally hypothesized that when values stop coming in, the GCE would gap fill in what is missing, but due to the glitch in MATLAB datetime objects is getting a rounding error. But on other sites, like this VARAMET, the data disappears from METDAT at least a full hour earlier than the date-number gets "off" on the Portal. And on the opposite extreme, the majority behavior is as expected: the data is missing, flagged as such, marked as NaN, and also METDAT has a full stream of NULL values. 

If we look back to the prior hour on Portal,  the data behaves as we expect 

        "VARMET",2014-09-21 06:00:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:05:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:10:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:15:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:20:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"

In this set, the 4th column from the right end should be "snow depth." It is NaN. In METDAT, it is not there, so it is NULL. But if I open the table VAN_228__inlocs__, I see exactly one record in that 3 hour interval between 6 and 9 am on that day, which is: 

        TmStamp RecNum  PRECIP  PUMPVOLTS   AIR_450 RAW_DIST    SWE BATTERY_V   TKELVIN REF_TEMP    MULT1   DISTTOSNW   DISTTOGND   SNOWDEPTH   OR_TEMP CON_TEMP    RUN_TIME    LOGGERID    PROGID  QUALITY

        2014-09-21 06:18:47.8000000 33  39.45435    12.87784    18.4769-0.4315314   12.33467    291.6269    273.15  1.033268    0   5.6 5.6 17.4444 4   900 301 35  0


So, some measurement is being recorded for "snow depth" and if I am counting right it is "5.6" in this case. But that is the only measurement in that window. I "googled" \_inlocs\_ to try to understand their role in logger-net and it seems like this table is generated "whenever the logger is checked for data"-- what that means, I do not really know. But it also doesn't seem to be very consistent, for example, when the data is missing from 2012-12-21 15:25 to 2012-12-26, the last entry in \_inlocs\_ is at 10:04 am and it doesn't register again until 13:45 on 2013-01-02.

Further (03-01-2015) investigation into this issue has revealed that we have some severe quality issues with this particular VARAMET file. We are awaiting response on what post-processing has been done in order to proceed.