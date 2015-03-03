---
layout: post
title: "Notes on flags for Air Temperature, Relative Humidity, VPD, Solar, and Wind (Speed and Direction) in Portal"
date: 2015-02-20T14:09:55-08:00
---

This is a list of all the checks which were in place in Portal, and a growing list of those which we think should be added. In some cases, I've condensed the checks down, for example, I'll only show 1 height for the air temperature, etc. 

In the 2015 files for air-temperature, all NaN values are juxtaposed with "M"! :)

For all flags, these are just on the five minute data

AIR TEMPERATURE
-------

* In place:
    * if airtemp < 35 or > 50, "I"; if airtemp < -18 or > 45, "Q", if value change between two intervals > 6.5 on either side, "V"; if value change between two intervals > 8 on either side, "IV", if NaN, "M", if lower than four-sigma, "Q", if above four-sigma, "Q"

* Add:
    * Add propogatation from the air temperature into the dependant flags of dewpoint, vpd, etc. Do not propogate to relative humidity. For example, if air temperature is "M", dew point is "M". If air temperature is "Q", dewpoint is "Q". 

* Consider:
    * Using air temperature to mark questionable values for precipitation, snow, or solar? Helpful for detecting certain events or balance between radiative components?

DEWPOINT
-------

* In place:
    * Flags from airtime are propagated to dewpoint (i.e. if air temperature is "M", so is dewpoint)

* Add:
    * If dewpoint > airtemperature, flag as "I"
    * Relative humidity flags propogate to dewpoint
    * If either air temperature and relative humidity is missing, dew point is missing; if either air temperature or relative humidity is questionable, dew point is questionable.
    
    
RELATIVE HUMIDITY
--------

* In Place:

    * Flags from airtemp are propagated to here - this is not correct!

* Add:
    * Remove flag propagation from air temp. 
    * Add "Q" flag for persistent values of 100 % humidity for 4 or more days as shown 
    * Add a basic percentage flag, impossible values of it can't be > 100, can't be < 0.
    * Add a step change flag: relative humdity can't change more than 10 percent per five minutes is very safe. Be sure that step change is not including stepping onto or off a "NAN"

SONIC MEAN WIND DIRECTION
----------------

* In Place:
    * If direction is less than 0 or > 360, "I"; if is NaN, "M"; Standard deviations of > 180 are "Q", those of < 0 are "Q".

* Add:
    * If direction is NaN, "M" or if speed is "M" or "I", then the direction should be "Q"(maybe "M" if speed is "M"?). 
    * Don suggests to receive propogated flags from mean speed. 
    * If the STD of direction is "Q" then the direction should also be "Q", since this indicates errors at the higher resolution of the collected data.
    * If the temperature of the sonic is "M" the direction should be "M". 
    * If the temperature of the sonic is "I" or "Q" the direction should be "Q".
    * If the component winds (either wux or wuy) are "M" then the direction should be "Q" (since it needs the component winds)
    * If any system flag (battery, etc.) is thrown, then the sonic direction is Q.
    * NEW ADDITION: If the number of points sampled and good (not "M", "I", or "Q") is less than 60 percent of the total number of points that should be sampled, the measurement should be "Q". This comes from how Chris identified relevant windows and I think it's valid here too.


SONIC MEAN WIND SPEED:
------

* In place
    * NaN values are "M", > 15 is "Q"

* Add: 
    * When sonic mean is "I" replace Sonic Max Flag wih "Q", When sonic mean is "I", replace sonic x-vector and y-vector with "Q". Receive propogated "M" flag from mean speed. 
    * for x and y vectors speed, replace "I" values with M when values are missing from speed or themselves. 
    * if direction is "M" or "Q", speed should be also "M" or "Q"
    * if < 60% of high-resolution measurements were used to compute five minute means, flag as "Q"


SONIC MEAN WIND STANDARD DEVIATION:
---------

* In place
    * NaN values are "M", components with > 10 are I. 

* Add
    * When sonic mean speed is "I", replace mean STD with "Q
    * When sonic x-vector or y-vector is is "I", replace mean std with "Q"
    * Supplement the sonic mean standard deviation with the sonic mean wind speed when the standard deviation is blank but the mean wind speed is not blank (instead of a 0 value). Flag with a "Q"
    * Receive propogated "M" flag from mean speed. 
    * I do not think it is possible to have a negative standard deviation, since it's the square root of the variance. Remove.
    * Apply system flags for battery, etc. to "Q" values that might be bad. See sonic temp for details. 

SONIC MEAN TEMP:
------------

* In place
    * NaN values are "M"

* Add
    * If sonic temp is "I" then replace sonic mean, sonic x-vector, sonic y-vector, sonic direction, sonic std direction with "Q" 
    * If the sonic air temperature standard deviation flag is blank replace it with the sonic air temperature flag. Receive propogated "M" flag from mean speed. 


SOIL TEMP MEAN
--------------

* In place:
    * if soil temp < -2, "I"; if soil temp > 35, "I"; if soil temp < -1, "Q", if > 30, "Q", if NaN, "M"
    
* Add:
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

* In place:
    * if gust is NaN, flag "M".

* Add:
    * if mean wind is NaN, gust is "Q", what is based on?
    * Some of these gusts seem far too high, on the order of 35 + mph. Should get information on these spikes.
    * if mean wind is "Q", gust is "Q"; if mean wind is "M", gust is "M"; if mean wind is "I", gust is "Q"
    
    
SONIC MEAN:
---------

* In place: 
    * if mean wind is < 0, "I"; if mean wind is NaN, "M"
* Add:
    * if mean wind is "I" or "M", gust, direction, and component winds are also "I" or "M", at worst, "Q"
    
    
SONIC DIRECTION DEVIATION
------------------

* In place:
    * if deviation is NaN, "M"
* Add:
    * if direction is NaN, "M"; if speed is NaN, "Q"
    
VPD
-----

* In place:
    * flags propogate from Air Temperature

* Add:
    * flags should also propagate from Relative Humidity
    
VAP
------

* In place:
    * flags propagate from Air Temperature
* Add:
    * flags should also propagate from Relative Humidity
    
SOIL WATER CONTENT
-----------------

* In place:
    * if it is NaN, "M"
* Add:
    * if soilwc < 0, "I"; if soilwc > 1.0, "I" (it's a percent)
    * if soilwc > 0.5, "Q" 
    
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

* In place:
    * if speed is less than 0.3, "N"; if speed is less than 1, "B"; if speed is more than 20, "I"; if speed is more than 15, "Q"; if speed is NaN,"M"
 
*Add:
    * if speed is NaN or I, then direction, and direction STD, they should also be "M" or "I"
    * if speed does not change for a certain period of time flag (will do some tests- FSP)
    * if temperature is < 0 and speed is 0, "Q" (frozen?)
 
WIND DIRECTION ON THE PROP
-------------
 
* In place:
    * if direction < 0 or > 360, "I"; if direction is NaN, "M"

* Add:
    * if direction is NaN, direction deviation is NaN, speed is "Q"
    
WIND DIRECTION DEVIATION ON THE PROP
----------------

* same as suggestions for sonic


SOLAR SW IN
---------------

* In Place:
    * Remove values > and < 2000 and -2000 and flag with 'I'
    * Flag values >1060 'Q'.
    * Set incoming and outgoing shortwave rad to zero when incoming shortwave rad is <1.
    * Set albedo to NaN when incoming shortwave rad is <1

* Add:
    * Negative values are set to zero for values < 0 and >-5 with no flag for both incoming and outgoing shortwave when time is between 1600 and 0900.
    * Change values <0 to zero when time is between 0900 and 1600, flag with 'Q'.
    * Set negative values <-5 to zero and flag with 'Q' when time is between 0900 and 1600.
    * Incoming shortwave values greater than 2 would remain and be flagged as 'Q' when time is between 2100 and 0500.
    * Recompute net radiation and flag value as Q if any of the four components are flagged with a ‘Q’.
    * Albedo is "I" if albedo > 0.95 (earth is not black body radiator!)


SOLAR SW OUT
--------------

* In Place:
    * Outgoing shortwave rad to zero when incoming shortwave rad is <1.

* Add:
    * Outgoing shortwave values greater than 2 would remain and be flagged as 'Q' when time is between 2100 and 0500.
    * if albedo is Q (due to SW in being too small), SW out is Q.
    * SW out is 0 at night


SOLAR LW IN 
------------

* In Place:
    * None

* Add:
    * If LW in > LW out, "Q"


SOLAR LW OUT
--------------

* In Place:
    * None

* Add:
    * At night, LW out should always be > SW in, SW out, and LW in. If not all get the "Q"