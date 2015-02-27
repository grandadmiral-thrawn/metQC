---
layout: post
title: "Notes on Flags in Portal Part 2, Precipitation and Snow"
date: 2015-02-20T09:44:00-08:00
---

The following are notes and examples regarding the five-minute precipitation, snow-melt, and snow-depth flags. This currently is a notes section that is under construction, and more may be added.

Convention: when I list a flag as "in place" that means it is on Portal and is being implemented as the description suggests. If I follow that with a description or example it shows a case where the flag is being implemented, but may have unintended consequences for another column. 

If I list a flag as "Add" these are flags that I think should exist but do not yet exist. In the case of aggregating to the daily I have not fully populated this list yet as I am still checking the daily to see what is actually in place, and that is much harder due to the inconceivable amount of attributes in the daily file. 

FLAGS ON PORTAL FOR PRECIP and SNOW
----------------

Here is a case of "worst case" missing values on CENMET 225, to show what propagates, in terms of flags. Note that some NaN's carry "M" while others do not.

        "CENMET_225",2012-05-20 16:25:00,NaN,"M", 225, NaN, "M", NaN, "M", NaN,"M", NaN, "" , NaN, "M", NaN, "M", NaN, "", NaN, "M", NaN, "M",  NaN, "", NaN, "", NaN, "M"


This is a record which is entirely missing from METDAT and so has been gap filled in by GCE:

Here is the METDAT:

        2012-05-20 16:20:00 1234    225 6141    2012    141 1620    70.7    101.3   7.95    0   -0.123  29.45   26.96   13.36   NULL
        
        NO RECORD HERE AT 16:25:00

        2012-05-20 16:30:00 1235    225 6141    2012    141 1630    70.6    101.1   8.309999    0   -0.127  29.44   26.45   13.34   NULL
        

* snow-depth median does not get flagged as "M" when there is NaN.
* swe-median does not get flagged as "M" when there is NaN
* the "precip diffs" do not get flagged as "M" when there is NaN.


Record Number:
------

* In place: 
    * if Record Number < 0, "I"; if Record Number is NaN, "M"
* Add:
    * if Record Number < 0, "I"; all other attributes should be "Q"
        * Rationale: indicates possibly catastrophic instrument issues
    * if Record Number is NaN, "M"; all other attributes also "M"
        * Rationale: if the record number is missing then its likely everything else is also missing
        
        

Program ID:
----------

* In place:
    * if it changes, "P".

* Add: 
    * if any "P" in a sub-daily file, the daily should also show a "P"
    * On the measurement of "P", all other measurements in that line should be a "Q", see this - notice how the SWE has gotten a "Q" appropriately because it is not a normal measurement, but why should we also trust the other measurements? After 2 times, it appears the system is good to go again.
    
### BAD
    
        "CENMET_225",2013-11-20 09:55:00,157098,"",225,950.0,"P",14.100,"", 21.470,"",0.00,"",204.000,"",51.14,"",0.00,"",5.688,"", 2224.00,"Q",-145.000,"",-146.00,"",0,""
    
    
### BAD
    
        "CENMET_225",2013-11-20 10:00:00,157099,"",225,950.0,"",14.750,"",  21.540,"",0.00,"",220.000,"",51.13,"",0.00,"",5.392,"", 2222.00,"Q",-145.000,"",-145.50,"",0,""
    
    
### OKAY!
    
        "CENMET_225",2013-11-20 10:05:00,157100,"",225,950.0,"",13.490,"",  21.540,"",0.00,"",197.000,"",51.35,"",0.00,"",      4.740,"",-1.61,"",-145.000,"",-145.00,"",0,""



Voltage:
---------

* In place:
    * if voltage < 0, "I"; if voltage < 12, "L", if voltage > 15, "H"
    * if voltage is NaN, "M"
* Add:
    * if voltage < 12; all other attributes "Q"
        * Rationale: impossible or low voltage indicates possibly catastrophic instrument issues
    * if voltage is NaN, "M"; all other attributes "Q"
        * Rationale: if the voltage is missing indicates possibly catastrophic instrument issues
        * Note: NaN is < 12, so really this could be one flag, if voltage < 12, all things are "Q"
        
    * algorithm on Q's and M's to assign a daily Q or M if too many values appear to be "bad"
        

Precip_Inst, orifice temperature, and precip_diff:
-----------

* for either SA or SH types
* In place:
    * If precip_inst > 0, "I"; if > 1200, "I", if value decrease is > 100, "R", if value increase > 25, "R"; if orifice temperature is < -2, "I"
    * if precip_inst is NaN, "M"
* Add:
    * if precip_inst is "M", precip_diff is also "M", orifice temperature is "Q"
    * if value increase is > 10, and previous record was not flagged, "Q", could be a snow bomb. precip_diff also "Q"
    * if value increase is > 10 and previous record flagged as "R", flag as "R". Precip diff is also "Q".
    * if precip inst is "I" due to range check or orifice temperature, prices diff should also be "I".
    * If precip diff < 0, "Q" - could be evaporation - use our algorithm.
    * If precip diff is NaN, it should get a "M"
    * implement algorithm to aggregate to daily.
    
SWE:
-----

* In place:
    * if SWE < -100, "I"; if SWE > 2500, "I", if SWE > 2000, "Q", if SWE os NaN, "M";
* Add:
    * should there be a flag to question the difference between SWE/snow-depth? 
    * should there be a flag on sharp changes in SWE?, maybe a value change of more than 50 at five minutes?
    * SWE NaN does not appear to always be getting the flag when it is "NaN". Is this because the NaN is being set post-hoc due to a manual change? If so, it should get an "M"
    
        "CENMET_225",2014-07-28 03:45:00, NaN, "M",225, NaN, "M", NaN, "M", NaN,    "M", NaN, "", NaN, "M", NaN, "M", NaN, "", NaN, "M", NaN, "M", NaN, "",     NaN, "", NaN, "M"

    
SNOWDEPTH:
----------

* In place:
    * if snow depth inst > 4500, then "I"; if > 4000 then "Q", if change of more than 0.5 over the past 12 intervals making the median then "I"; if NaN, "M"
    * Note: values here are being removed, see - the NAN is an I
    
        "CENMET_225",2012-06-13 13:30:00,5961,"",225,6430.0,"",13.270,"",   266.000,"",0.00,"",28.370,"",289.60,"",0.00,"",28.700,"",   104.20,"",NaN,"I",-103.00,"",0,""
    
* Add:
    * way to tell if snow depth was "not measured" or if there was no snow
    * if snow-depth is NaN, it should get an "M"

    
SNOW LYSIMETER:
--------------
* In place:
    * if snow lysimeter is < 0, "I"; if snow lysimeter is missing, "M"

* Add:
    * propagate missing snow lysimeters to the daily scale using algorithm
    