---
layout: post
title: "Outline of Flags and Problems on Portal"
date: 2015-02-08T16:11:30-08:00
---

This document gives short descriptions of the flags and their problems on the H.J. Andrews Portal website. While it primarily focuses on the discrepancies and flags in the suite of attributes of Air Temperature, Relative Humidity, Vapor Pressure Defecit, Vapor Pressure, and Dewpoint, examples from Precipitation, Snow Lysimeter, and Snow Water Equivalance are also given. Wind is only briefly mentioned in this document as its flags and consistency problems probably merit a separate analysis. Likewise, soil is not brought in here anywhere as we have already done a lot on it to pull it into the FSDB.

**Note:** Within this document I may use the terms "NULL", "NaN", and "None" interchangeably, to refer to data that does not have a value, but does have a type (such as "integer" or "string"). This is different from "empty" which might appear like this: '', ' ', "", " ", &nbsp, u'', U+00A0, etc...

How an "empty" is interpreted varies wildly, see [Wikipedia Article on WhiteSpace](http://en.wikipedia.org/wiki/Whitespace_character#Unicode) for more information. My goal here is just to point out that "empty" and "null" are NOT the same. Thus if I say a value is "missing" I will try to clarify whether the term means "given a 'NaN'-like term as a placeholder" or "given an empty" or actually just skipped entirely.

**Note:** Additionally, I tried to keep consistent naming and units when possible. AirT is Celcius air temperature, RH is relative humidity in percent, DEWPT is the dew point temperature in Celcius, VAP is the Vapor Pressure is the equilibrium vapor pressure in millibars (mb), SATVP is saturated vapor pressure in millibars, and VPD is the vapor pressure defecit, also in millibars. Precipitation is in millimeters for both snow and rain. Solar radiation here is not discussed in depth, but Photosynthetically Active radiation (PAR) is in millimols-photons per meters squared per second, and incoming photons take the negative convention. 

**A final note:** These are only examples of the types of problems seen. Once a production environment has been set up that checks for these errors, we will conduct more extensive follow up. 

# Table of Contents
  * [Existing flag codes](#flagcodes)
  * [Synchronized Flags across AIRT, DEWPT, VPD, RELHUM and VAP](#symlink)
  * [The very bad week of 2014-08-22 to 2014-08-26](#badcen)
  * [When flag value change is thrown in a case that is better described by impossible value](#imposs)
  * [When a missing flag on air temperature destroys other values and flags for that Date time, and those other values and flags represent likely impossible data](#missdestroy)
  * [When a existing value on air temperature is deemed impossible and destroys existing and possible values on other attributes](#missdestroy2)
  * [Estimated values for Air Temperature are not also estimated for other attributes when only one datetime is missing.](#estimated)
  * [There are values of Dew Point on Portal when both relative humidity and air temperature are missing](#whydew)
  * [The EI flag](#whatisei)
  * [IQVIQ flag](#whatisiqviq)
  * [High Elevation Removals](#notremoved)
  * [Flag Value Change Too Agressive at a Daily Scale](#fvc)
  * [Missing Values (NaN) not necessarily paired with "M" flags](#missing)


## Existing flag codes<a id = "flagcodes"></a>

Flag Codes may be combined with one another, to make a very long string of flags. A recently implemented "X" flag for manual has not been observed in the wild as of today (02-09-2014).

**A general note**: If a less stringent flag is caught within a more stringent flag, both flags will be displayed. Some combinations of flags have special meanings and are grouped together.  

* **B**: BELOW DETECTION LIMITS

    Below detection limits, on windspeed attributes on the propeller anemometers this means between 0.1 and 0.3 m/s.

* **NB**: NOT BELIEVE-ABLE? 

    Windspeed attributes that are less than 0.1 m/s.

* **T**: TOOLS?

    A general purpose flag on preciptiation data regarding human intervention. See [CENMET 225 2013-10-02](http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_225_5min_2014.csv)

* **I**: IMPOSSIBLE VALUE

    Air temperature is below - 35 deg C or above 50 deg C OR a subsequent air temperature value is at least 8 deg C above or below the preceding 5 minute value (in this case will be prefaced by "V"). When air temperature is with relative humidity, vapor pressure deficit, or dewpoint, this flag is always carried into the vapor pressure, dew point, and vapor pressure defecit attributes and often (erroneously) into the relative humidity attributes. For SWE, values of less than 100 mm or greater than 2500 mm are I. For Solar, values of less than 0 W/m2 or greater than 2000 W/m2 are I. For Windspeed, values of greater than 20 or less than 0 are I. All other values inherit from Air Temperature or do not have an I flag.

* **MM** : DOUBLE-MISSING

    Seen "in the wild" on CENMET only, it appears that on air temperature the "M" flag for NaN is thrown twice, so in all cases, "MM" will appear rather than just "M". Otherise, single "M"s (see below).


    ... flag_valuechange(x,8,8,1) ="I", isnan(x)="M", x<FOURLO="Q", x>FOURHI="Q", isnan(x)="M") ...

* **VI** : FLAG VALUE CHANGE, IMPOSSIBLE

    A subsequent air temperature value is at least 8 deg C above or below the preceding 5 minute value. Catches the "V" flag. When applied to air temperature, this flag is carried into the vapor pressure, dew point, vapor pressure defecit, and (sometimes) relative humidity attributes.

* **V** : FLAG VALUE CHANGE, ALL

    Flag value change- subsequent value differs from it's precursor; when on air temperature, relative humidity, vapor pressure defecit, dewpoint, or vapor pressure it is followed by a qualifier of "Q" (questionable) or "I" to describe the extent of discrepancy.
    A subsequent air temperature value is at least 6.5 deg C above or below the preceding 5 minute value.
    An example of not being described is on PAR, where "V" gets thrown to show photosynthetically active radiation value is different from its precursor, but the amount is unstated.

* **M** : MISSING FLAG

    "M" can carry over to dependent attributes, however CURRENTLY AN "M" in AIR TEMPERATURE will WIPE OUT relative humidity and other attributes. Can appear on the dependent attributes if the calculated values, such as of vapor pressure, dew point, vapor pressure defecit if they are uniquely missing, but air temperature is not. Will never appear on air temperature alone in CENMET in the current state (01-28-2015). Should be associated with NaN but isn't always.

* **VM** : Value Change on one attribute, missing on a dependency

    When a dataset contains air-temperature, the air temperature value throws a flag value change of at least 6.5 degrees variance, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing.


* **VIM** : VALUE CHANGE IS IMPOSSIBLE, and a DEPENDENCY IS MISSING

    When a dataset contains air-temperature, the air temperature value throws a flag value change of at least 8 degrees variance OR the air temperature value throws an I flag and the value change of air temperature from the previous is less than 8 degrees but more than six degrees, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing.


* **IQVIQ** : "The Mother-Lode" flag that often gets thrown when potentially useful values are seen in a strema of nan's.

    A flag that appears to get thrown when a value is preceded by an impossible (and therefore also questionable and flag-value-change impossible and flag-value-change questionable) and that value, in Portal, is a Nan. I.e. Temperature 1 is -31.0, Temperature 2 is NaN, Temperature 3 is 75.0. Temperature 2 in this case would get an IQVIQ, although it appears to be "missing" in the Portal. See the IQVIQ section.

* **E**: ESTIMATED

    A value is estimated based on the values around it, using a linear interpolation. Requires that only one value is missing, and does not affect dependent columns.

* **EI**: ESTIMATED IMPOSSIBLE

    There really is no reason for this flag, see the [EI section](#whatisei)

* **ER**: ESTIMATED RESET

    The ER flag appears prior to the R flag on the CS2MET precipitation


* **L**: Battery Voltage, Low

    The L flag apparently indicates low volatage, but it is not clearly documented.

* **H**: Battery Voltage, High

    The H flag apparently indicates high volatage, but it is not clearly documented.

## Synchronized Flags and NaN's across AIRT, DEWPT, VPD, RELHUM and VAP<a id="symlink"></a>

Air temperature, relative humidity, dew point, vapor pressure, vapor pressure defecit (VPD) are not synchronized. Quality or missing flags from air temperature and relative humidity should be passed along to the calculated dew point and VPD data.

A few examples are fully "fleshed out" here showing the distribution of different flag codes as well as relevant examples. These are some of the problems of non-synchrony seen on CENMET.

### CENMET(2014), summary of flags:

| 150 M |
|:--|:----|:--:|
| **Attribute** | **How many of each flag** | ** Total Flags **|
| Air Temperature |'MM':11,'VI':3,'V':5 | 19 |
| Relative Humidity | 'MM':10, 'VI': 1, 'M':5, 'VM':4, 'VIM':2, 'V':1 |  23 |
| Dew Point | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure Defecit | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure | 'MM':11, 'VI', 'M':1, 'VM':5, 'VIM':2, 'V':1  | 24 |

### We need to get rid of the bad week of 2014-08-22 to 2014-08-26 on CENMET<a id="badcen"></a>

The week of 2014-08-22 to 2014-08-26 is oddly behaved at CENMET. For example, here is a snippet from that week as found in METDAT database:

|TmStamp | AirT[C] | VAP[mb]| SATVP[mb] | DEWPT[C] | RH[%] |
|-|-|-|-|-|-|
| 14:05:00 | NULL | NULL | NULL | NULL | NULL |
|14:10:00 | NULL |  NULL |  NULL |  NULL |  NULL |
|14:15:00 | NULL |  NULL |  NULL |  NULL |  NULL |
|14:20:00 | -76.48 | -0.494 | 2.051 | 2.544 | -34.33 |
|14:25:00 | NULL |  NULL |  NULL |  NULL |  NULL |
|14:30:00 | 19.6 |  16.36 | 25.82 | 9.46 |  59.18 |
|14:35:00 | NULL |  NULL |  NULL |  NULL |  NULL |
|14:40:00 | -49.51 | 0.007 |0.134 | 0.127 | -8.73 |
|14:45:00 | -22.76 | 0.234 | 1.124 | 0.89 | 17.53 |
|14:50:00 | -12.18 | 0.682 | 2.425 | 1.743 |27.94 |
|14:55:00 | -13.36 | 0.759 | 2.495 | 1.736 | 26.71 |

and here is the corresponding hour and its flags, from the PORTAL

|TmStamp | AirT[C] | VAP[mb]| SATVP[mb] | DEWPT[C] | RH[%] |
|-|-|-|-|-|
|14:00 | nan | 'MM' | nan | 'MM' |
|14:05 | nan| 'MM' | nan | 'MM' |
|14:10 | nan| 'MM' | nan | 'MM' |
|14:15 | nan| 'MM' | nan | 'MM' |
|14:20 | nan| 'MM' | nan | 'MM' |
|14:25 | nan| 'MM' | nan| 'MM' |
|14:30 | 19.600 | no flag | 59.18 |no flag |
|14:35 | 13.008 |'V'| nan | 'VM' |
|14:40 | 6.416  |'V'| nan | 'VM' |
|14:45 | -0.176 |'V'| nan | 'VM' |
|14:50 | -6.768 |'V'| nan | 'VM' |
|14:55 | -13.36 |'V'| 26.71 | 'V' |

The Portal data differs from the METDAT data, not only in what is displayed and not displayed but also in the displayed values. See the entry for AirT[C] above at 14:40 as an example. 

### We need to fix or change the procedure to determine when flag value change is thrown in a case that is better described by impossible value.<a id="imposs"></a>

There are also problems in why flags are being thrown. Here, for example, are values on 2014-08-27 in the Portal:

| Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] |
|-|-|-|-|-|
| 08:20 | -11.060 | no flag | 28.810 | no flag |
| 08:25 | -15.116 | no flag | 24.880 | no flag |
| 08:30 | -15.440 | no flag | 24.540 | no flag |
| 08:35 | -5.403 | 'VI' |  nan | 'VIM' |
| 08:40 | 4.633 | 'VI' |  nan | 'VIM' |
| 08:45 | 14.67 | 'VI' | 87.2 | no flag |
| 08:50 | 14.730 | no flag | 87.5 | no flag |


A 'VI' flag is thrown indicating a flag for an impossible value change between a value of -15 C and -5 C. While this is certainly a strange jump, the error should not be thrown because of the jump, but rather because all the sensors were recording a week of sub-zero temperatures in August. 


### We need to figure out why sometimes a missing flag on air temperature "destroys" other values and flags for that date time, first in the case of when hose other values and flags represent likely impossible data...<a id="missdestroy"></a>

Another notable problem is when the 'M' flag for air temperature appears to "wipe out" the potentially acceptable value of relative humidity. Although this week on CENMET was odd, it does show a good example of how an impossible temperature anihilates humidity with an "M" flag.

Here is the data from METDAT:

|TmStamp | AirT[C] | VAP[mb]| SATVP[mb] | DEWPT[C] | RH[%] |
|-|-|-|-|-|-|
| 13:55:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:00:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:05:00 | -82.7 |  1.573 | 0.874 | NULL |  -40.98 |
| 14:10:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:15:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:20:00 |  -59.64 |  0.799 | 2.133 | NULL |  -18.75 |
| 14:25:00 |  -11.56 |  3.869 | 9.34 |  NULL |  28.48 |
| 14:30:00 |  -36.71 |  0.692 | 1.01 |  NULL |  3.768 |
| 14:35:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:40:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:45:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:50:00 |  NULL |  NULL |  NULL |  NULL |  NULL |
| 14:55:00 | NULL | NULL |  NULL |  NULL |  NULL |

Note between 14:20 and 14:30, where relative humidity, even when odd, does exist.  Here is that same hour on Portal.

| Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] |
|-|-|-|-|-|
| 13:55:00 | nan | MM| nan | MM|
| 14:00:00 | nan | MM| nan | MM|
| 14:05:00 | nan | MM| nan | MM|
| 14:10:00 | nan | MM| nan | MM|
| 14:15:00 | nan | MM| nan | MM|
| 14:20:00 | nan | MM| nan | MM|
| 14:25:00 | nan | MM| nan | MM|
| 14:30:00 | nan | MM| nan | MM|
| 14:35:00 | nan | MM| nan | MM|
| 14:40:00 | nan | MM| nan | MM|
| 14:45:00 | nan | MM| nan | MM|
| 14:50:00 | nan | MM| nan | MM|
|14:55:00 | nan | MM| nan | MM|

There are no values- nothing to indicate the impossible values clearly in METDAT, and even some of the possible pressures being calculated. 

### ... But as problematic is when an existing value on air temperature is deemed impossible, displays a NaN, and destroys existing and sometimes even possible values on linked attributes<a id="missdestroy2"></a>:

Here are the values on the Portal (2014-08-22):

|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] |
|-|-|-|-|-|
|10:45:00 | nan | MM | nan | MM |
|10:50:00 | nan | MM | nan | MM |
|10:55:00 | nan | MM | nan | MM |


And their corresponding values in METDAT:


| TmStamp | AirT[C]  |  VAP[mb] | SATVP[mb]| DEWPT[C] | RH[%] |
|-|-|-|-|-|
| 10:45:00| -37.42| 0.242 | 0.248 | -69.69 | 2.357| 
| 10:50:00 |-28.75| 0.528 | 0.596 | -50.74 | 10.5 |
| 10:55:00| -20.47| 0.991 | 1.215 | -38.55 | 18.23| 


### The persistance of the "E" flag for estimated values is limited. Estimations occur directly for Air Temperature, but other attributes that could be estimated are not.<a id= "estimated"></a>

Here is the entry in METDAT on 2014-11-11 19:45 to 19:55 on PRIMET, height 150.


|Time | AirT[C] | RH[%] | DEWPT[C]|
|- |- |- |- |
| 2014-11-11 19:45:00 | -0.853 | 84.5  | -3.133 |
| 2014-11-11 19:55:00 | -1.107 | 88.2  |-2.799 |


|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] | Dewpt[C] | flags on Dewpt[C]|
|- |- |- |- |-|- |-|
|2014-11-11 19:45:00 | -0.85|"" |84.500|""|-3.133 |""|
|2014-11-11 19:50:00 | -0.98 |"E" |NaN |""|NaN |""|
|2014-11-11 19:55:00 | -0.677|"" |88.20|""|-2.79 |""|

If temperature can be estimated based on the surrouding interval, it seems that if RELHUM is present, it can also be estimated, and if it can also be estimated, so can the calculated attributes of dewpoint, saturated vapor pressure, and vapor pressure.

### Sometimes there are values of Dew Point displayed on the Portal when both Relative Humidity and Air Temperature are missing <a id="whydew"></a>

** Also, the dew point is actually flagged as missing, despite being there.**


|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] | Dewpt[C] | flags on Dewpt[C]|
|- |- |- |- |-|- |-|
| 2014-05-09 00:00:00 |NaN |"M"| NaN | "M" | 7.960 |"M" |
| 2014-05-09 00:05:00 |NaN |"M"| NaN | "M" | 7.885| "M"|
| 2014-05-09 00:10:00 |NaN |"M"| NaN | "M" | 7.849 | "M"|


This is a very common error, but it is not universal. There are some times when the missing air temperature alone will kill both the relative humidity and the dew point, as previously discussed and exemplified. 

### EI flag does not really make any sense <a id="whatisei"></a>

I am not sure why an EI flag could get thrown on air temperature unless a flag-value-change threw "I" and value was placed in that gap, which appears to be what is going on, but it is unclear. Here is what is in Portal, on [VANMET_231_part1](http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VANMET/data/vanmet_231_a_5min_2015.html) at 450 m height.


|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] | Dewpt[C] | flags on Dewpt[C]|
|- |- |- |- |-|- |-|
| 2014-07-03 11:40:00 | 17.990 | "" | 63.800 | "" | 11.040 |"" |
| 2014-07-03 11:45:00 | 19.720 |"EI" | 64.990 |""| NaN |"VIM" |
| 2014-07-03 11:50:00 | 18.060 |"" |52.72| "" |11.360|""|


In METDAT, the first value is the same. Next, a flag value change of "I" gets thrown on the probably incorrect low value. It is re-estimated and an EI comes into the data. However, unlike the Portal, the subsequent measurement is not the same for temperature. 


  * Does this EI extend into the next measurement as well on Portal?
  * Why is relative humidity estimated for the 11:45 measurement on Portal, but not flagged also as E?
  * Why, if the air temperature and the relative humidity can be solved, is the dew point not being solved?


|Time | AirT[C] | RH[%] | DEWPT[C]|
|- |- |- |- |
| 2014-07-03 11:40:00 | 17.99 | 63.8 | 11.04 |
| 2014-07-03 11:45:00 | 6.542 | 41.18 | NULL |
| 2014-07-03 11:50:00 | 21.45 | 52.72 | 11.36 |


### IQVIQ is not appropriate really at any time, and should be either an "M" or an "I" in many cases <a id ="whatisiqviq"></a>

On Vanmet, Portal reports:


|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] | 
|- |- |- |- |
| 2014-12-30 00:45:00 | -13.500 |"" |91.000|""|
| 2014-12-30 00:50:00 | NaN | "IQVIQ" | NaN |"IQVIQ" |
| 2014-12-30 00:55:00 | NaN |"IQQ" | 85.900| ""|


METDAT reports the existance of seemingly impossible temperature values, but reasonable relative humidity values. In the row with IQVIQ, it appears that the temperature has wiped out the relative humidity value for that day.


|Time | AirT[C] | RH[%] | DEWPT[C]|
|- |- |- |- |
| 2014-12-30 00:45:00 |-13.5  | 91 |  -13.77 |
| 2014-12-30 00:50:00 |-38.57 |90.7 | -13.8 |
| 2014-12-30 00:55:00 |-38.56 | 89.9 |   -13.99 |


### Removal of High-Elevation Sensors, data is not flagged.<a id = "notremoved"></a>


I am unable to tell from the data the exact dates of winter removal, but suffice it to say that when data is up on Portal for H15 at 15 minutes, it is up throughout the 2013 year, and without flags. If these are the same days of removal as on UPLMET, there are also no flags, but the UPLMET files do have some flags in them, for preceding (May 2012, etc.) times.

The problem of having dew point and vapor pressure calculated even when the data itself was missing is still occuring, as shown above. 

There don't appear to be any flags at all on CS2MET.

H15MET is fully update in METDAT but is not on Portal. 

There is another whole document listing all the missing dates and times.


## Flag Value Change Is Too Agressive at a Daily Scale <a id 
="fvc"></a>

** Really, there is an issue regarding aggregate (daily and hourly) flags in general. Don's algorithm, which solves this problem, has not been implemented anywhere on Portal.**

It has been noted that the flag for value change of 6.5 C as questionable and 8 C as impossible is reasonable at a high resolution 5 or 15 minute scale but may not apply at the daily scale. It also seems to show up on the daily scale in odd places. Here are some examples:


| Station | Day | Height | AirT[C] | Flag |
|- |- |- |- |
| UPLMET | 2013-06-22 | 450 M | 14.64 | "" |
| UPLMET | 2013-06-23 | 450 M | 7.69 | "" |
| UPLMET | 2013-06-24 | 450 M | 4.74 | "" |


In this example, the dewpoint gets a flag value change, but all values of temperature and relative humidity are NaN's


| Station | Day | Height | Dewpt[C] | Flag | AirT[C] | Flag |
|- |- |- |- |
| UPLMET | 2012-05-02| 150 M | -0.80 | "" | NaN |"IQQI" |
| UPLMET | 2012-05-03 | 150 M | 6.72 | "V" | NaN |"IQQI" |
| UPLMET | 2012-05-04 | 150 M | 12.690 | "" | NaN |"IQQI" |


Here is an example of the "V" flag getting thrown on CENMET 15 minute data for Photosynthetically Active Radiation. It should be noted that surrounding this time, all the other sensors are outputting all NaN on the portal, but show values in METDAT. 


| Station | Date Time | Height | PAR AVG[mu-mols/m2 s] | Flag |
|- |- |- |- |
| CENMET_225| 2013-03-04 03:45:00 | 450 | -0.866 |""|
| CENMET_225| 2013-03-04 04:00:00 | 450 |-7.380 |"V"|
| CENMET_225| 2013-03-04 04:15:00 | 450 |-8.100 | ""|


I have also seen an example of how a persistance function was unable to move off the flag value change, and will need to refind this for another discussion.

## Missing Values (NaN) not necessarily paired with "M" flags <a id="missing">

** This is really one of the biggest problems, there is not really any consistency between the presence or absence of "M", NaN, or empties. The most problematic data sets are the ones with precipitation and snowdepth, it looks like the air data sets are better controlled. Since we are fixing the wind currently I have not addressed the missing wind values yet**

The missing flag "M" should accompany NaN values. In this case, the SWE and snow-lysimeter attributes on the five minute CENMET logger are not being marked. There are other examples as well. Rows are shown here with the headers due to the length of the rows and the multiple NaN and "M" flag combinations. First row is the headers, second is a good row, third is a bad row.


    "Site","Date","RecNum","Flag_RecNum","LOGGERID","PROGID","Flag_PROGID","BATTERY_INST","Flag_BATTERY_INST","PRECIP_INST_455_0_01","Flag_PRECIP_INST_455_0_01","PRECIP_DIFF_455_0_01","Flag_PRECIP_DIFF_455_0_01","ORI_SA_AVG","Flag_ORI_SA_AVG","PRECIP_INST_625_0_02","Flag_PRECIP_INST_625_0_02","PRECIP_DIFF_625_0_02","Flag_PRECIP_DIFF_625_0_02","ORI_SH_AVG","Flag_ORI_SH_AVG","SWE_INST_0_0_01","Flag_SWE_INST_0_0_01","SNODEP_INST_0_0_01","Flag_SNODEP_INST_0_0_01","SNODEP_MED_0_0_01","Flag_SNODEP_MED_0_0_01","LYS_TB_TOT","Flag_LYS_TB_TOT"

    CENMET_225, 2012-05-23 16:00:00,2092,"",225,6141.0,"",13.120,"",113.200,"",0.00,"",10.090,"",140.60,"",0.00,"",10.390,"",127.00,"",-134.000,"",-135.00,"",0,""

    CENMET_225, 2012-05-23 16:05:00,NaN,"M",225,NaN,"M",NaN,"M",NaN,"M",NaN,"",NaN,"M",NaN,"M",NaN,"",NaN,"M",NaN,"M",NaN,"",NaN,"",NaN,"M"


Here is a similar example from CS2MET:

    "Site","Date","RecNum","BATTERY_MIN","Flag_BATTERY_MIN","ActTemp","Flag_ActTemp","PPT_N4_INST","Flag_PPT_N4_INST","PPT_N4_DIFF","Flag_PPT_N4_DIFF","PPT_N4_AVG","Flag_PPT_N4_AVG"

    "CS2MET_CLRG",2010-12-14 20:45:00,11,13.04,"",21.18,"",98.1611,"",0.00,"",98.1852,""

    "CS2MET_CLRG",2010-12-14 21:00:00,NaN,NaN,"M",NaN,"",NaN,"",NaN,"",NaN,""

    "CS2MET_CLRG",2010-12-14 
    21:15:00,NaN,NaN,"M",NaN,"",NaN,"",NaN,"",NaN,""

    "CS2MET_CLRG",2010-12-14 21:30:00,NaN,NaN,"M",NaN,"",NaN,"",NaN,"",NaN,""

Here is a nice mixed "M" flagged NaN row with non-flagged NaN's, and an "E":

    "Site","Date","RecNum","LOGGERID","PROGID","PRECIP_ORIF_455_0_02","Flag_PRECIP_ORIF_455_0_02","PRECIP_INST_455_0_02","Flag_PRECIP_INST_455_0_02","PRECIP_DIFF_455_0_02","Flag_PRECIP_DIFF_455_0_02","SNODEP_QUAL","SNODEP_INST_0_0_05","Flag_SNODEP_INST_0_0_05","SNODEP_MED_0_0_05","Flag_SNODEP_MED_0_0_05","SWE_MEAN_0_0_05","Flag_SWE_MEAN_0_0_05"

    "VARMET",2012-05-21 14:40:00,1,0,2021.0,8.54,"",41.90,"",0.37,"",NaN,74.0000,"",75.50,"",173.9555,""

    "VARMET",2012-05-21 14:45:00,NaN,0,2021.0,NaN,"M",41.96,"E",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"

    "VARMET",2012-05-21 14:50:00,2,0,2021.0,8.64,"",42.02,"",0.00,"",NaN,81.0000,"",77.00,"",173.7116,""


## Ultimately, in terms of flagging the following issues should be touched:

* "M", NaN, and Empty should be consistent in all data sets
* Daily and hourly aggregates should not be based on five minute functions
* Flag propagation from air-temperature must not destroy independent relative humidity measurement
* Human-altered flags need to be made clear