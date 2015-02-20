---
layout: post
title: "Checks on Air Temperature and Wind in Portal"
date: 2015-02-20T14:09:55-08:00
---


In the 2015 file, all NaN are met with "M"! :)

AIRTEMP
-------

* In place:
    * if airtemp < 35 or > 50, "I"; if airtemp < -18 or > 45, "Q", if value change between two intervals > 6.5 on either side, "V"; if value change between two intervals > 8 on either side, "IV", if NaN, "M", if lower than four-sigma, "Q", if above four-sigma, "Q"

* Add

DEWPOINT
-------

* In place:
    * Flags from airtime are propagated to here
* Add:
    * if calculating using the logger instruction, the dew point temperature must be less than air temperature (check against some random values)
    * Relative humidity flags propogate to dewpoint
    * If either air temperature and dew point missing, dew point is missing
    
    
RELATIVE HUMIDITY
--------

* In Place:
    *Flags from airtemp are propagated to here
* Add:
    * Remove flag propagation from air temp. 
    * Add "Q" flag for persistent values of 100 % humidity for 4 or more days as shown 


SONIC MEAN WIND DIRECTION
----------------

In Place:
* If direction is less than 0 or > 360, "I"; if is NaN, "M"

Add:
* If direction is NaN, "M"; is speed is "M" or "I", direction is "Q"(maybe M or I)

SONIC MEAN WIND STANDARD DEVIATION:
---------

In place:

Add:
* if direction is NaN, "M"
* if deviation is 0, "Q"
* if deviation is NaN, "M"

SOIL TEMP MEAN
--------------

In place:
    * if soil temp < -2, "I"; if soil temp > 35, "I"; if soil temp < -1, "Q", if > 30, "Q", if NaN, "M"
    
Add:
    * I wonder about that lower limit on temperatures, the limit of our system is down to -35 C and although I don't think it's likely it gets that cold, at 10 cm, I think we could go below -2 reasonably.
    * If any one soil temp is more than 10 C different than the others?
    
    
    For example, this looks wrong
    
        sqlite> select Date, SOILTEMP_MEAN_0_100_04,        SOILTEMP_MEAN_0_10_01, SOILTEMP_MEAN_0_20_02,       Flag_SOILTEMP_MEAN_0_20_02, SOILTEMP_MEAN_0_50_03 from fiveCenmet       where Date > 2015-01-01 limit 10;
            
        2014-12-12 05:20:00|6.756|5.936|20.170||5.835
        2014-12-12 05:25:00|6.756|5.935|20.170||5.835
        2014-12-12 05:30:00|6.756|5.934|20.190||5.835
        2014-12-12 05:35:00|6.757|5.933|20.200||5.837
        2014-12-12 05:40:00|6.757|5.932|20.200||5.837
        2014-12-12 05:45:00|6.757|5.930|20.200||5.837
        2014-12-12 05:50:00|6.757|5.930|20.190||5.838
        2014-12-12 05:55:00|6.757|5.929|20.180||5.838
        2014-12-12 06:00:00|6.758|5.928|20.170||5.838
        2014-12-12 06:05:00|6.758|5.926|20.170||5.838
            
SONIC GUST
----------

In place:
    * if gust is NaN, flag "M"
Add:
    * if mean wind is NaN, gust is "Q", what is based on?
    
    
SONIC MEAN:
---------

In place: 
    * if mean wind is < 0, "I"; if mean wind is NaN, "M"
Add:
    * if mean wind is "I" or "M", gust, direction, and component winds are also "I" or "M", at worst, "Q"
    
    
SONIC DIRECTION DEVIATION
------------------

In place:
    * if deviation is NaN, "M"
Add:
    * if direction is NaN, "M"; if speed is NaN, "Q"
    
VPD
-----

In place:
    * flags propogate from Air Temperature

Add:
    * flags should also propagate from Relative Humidity
    
VAP
------

In place:
    * flags propagate from Air Temperature
Add:
    * flags should also propagate from Relative Humidity
    
SOIL WATER CONTENT
-----------------

In place:
    * if it is NaN, "M"
Add:
    * if soilwc < 0, "I"; if soilwc > 1.0, "I" (it's a percent)
    * if soilwc > 0.5, "Q" (except in a pile of litter it's pretty unlikely soil WC is going to be > 0.5, we are an andisol after all).
    
    
    see here, an example of a few measurements of soil WC
    
    sqlite> select SOILWC_MEAN_0_100_04, SOILWC_MEAN_0_50_03, SOILWC_MEAN_0_20_02 from fiveCenmet limit 10

        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        0.235|0.255|0.177
        
        
WIND SPEED ON THE PROP
-----------------

In place:
 * if speed is less than 0.3, "N"; if speed is less than 1, "B"; if speed is more than 20, "I"; if speed is more than 15, "Q"; if speed is NaN,"M"
 
 Add:
 * if speed is NaN or I, then direction, and direction STD, they should also be "M" or "I"
 * if speed does not change for a certain period of time flag (will do some tests- FSP)
 * if temperature is < 0 and speed is 0, "Q" (frozen?)
 
 WIND DIRECTION ON THE PROP
 -------------
 
 In place:
    * if direction < 0 or > 360, "I"; if direction is NaN, "M"

Add:
    * if direction is NaN, direction deviation is NaN, speed is "Q"
    
WIND DIRECTION DEVIATION ON THE PROP
----------------

* same as suggestions for sonic