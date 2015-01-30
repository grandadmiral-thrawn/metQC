---
layout: post
title:  "Checks on GCE_to_FSDB Document"
date:   2015-01-30 14:57:30
categories: GCE date checks
---

Checks on GCE_to_FSDB Document
-----------------------------

The purpose of this analysis is to review possible changes and fixes in the GCE output .csv files that may affect data quality in FSDB. My role was to review potential problems in the GCE output, see if those problems were fixed, and see if the fixes were propogating into future outputs. To do this I developed my own toolkit which replicated the graphical properties of GCE, and also allowed comparisons across datafields.

**Note:** Within this document I may use the terms "NULL", "NaN", and "None" interchangeably, to refer to data that does not have a value, but does have a type (such as "integer" or "string"). This is different from "empty" which might appear like this: '', ' ', "", " ", &nbsp, u'', U+00A0, etc...

How an "empty" is interpreted varies wildly, see [Wikipedia Article on WhiteSpace](http://en.wikipedia.org/wiki/Whitespace_character#Unicode) for more information. My goal here is just to point out that "empty" and "null" are NOT the same.

**Note:** Additionally, I tried to keep consistent naming and units when possible. AirT is Celcius air temperature, RH is relative humidity in percent, DEWPT is the dew point temperature in Celcius, VAP is the Vapor Pressure is the equilibrium vapor pressure in milli-bars (mb), SATVP is saturated vapor pressure in milli-bars, and VPD is the vapor pressure defecit, also in millibars. 

**Note:** The order of data by station is usually CENMET, VANMET, PRIMET, H15MET, UPLMET, and CS2MET. Analysis is done on the finest resolution data possible, if not specified.

# Table of Contents
  * [(incomplete)Synchronized Flags across AIRT, DEWPT, VPD, RELHUM and VAP](#symlink)
  * [(incomplete)Wintertime removals not reflected on all attributes](#nanlink)
  * [(incomplete)Questionable Values with no rationale](#qvals)
  * [(incomplete)Step Test for 'V' flags](#vvalsday)
  * [(incomplete)Missing Times](#misstimes)

## Synchronized Flags and NaN's across AIRT, DEWPT, VPD, RELHUM and VAP<a id="symlink"></a>

Air temperature, relative humidity, dew point, vapor pressure, vapor pressure defecit (VPD) are not synchronized. Quality or missing flags from air temperature and relative humidity should be passed along to the calculated dew point and VPD data.

Flag Codes, at 5 minutes. If a less stringent flag is caught within a more stringent flag, both flags will be displayed. 

* I: An air temperature is below - 35 deg C or above 50 deg C OR a subsequent value is at least 8 deg C above or below the preceding 5 minute value. This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes.
* MM : On air temperature the "M" flag for NaN is thrown twice, so in all cases, "MM" will appear rather than just "M". This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes. 
* VI : A subsequent air temperature value is at least 8 deg C above or below the preceding 5 minute value. Catches the "V" flag from this case. This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes.
* V : A subsequent air temperature value is at least 6.5 deg C above or below the preceding 5 minute value.
* M : Will never appear on air temperature alone in the current state (01-28-2015). Can appear in vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes if they are uniquely missing, but air temperature is not.
* VM : The air temperature value throws a flag value change of at least 6.5 degrees variance, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing. 
* VIM : The air temperature value throws a flag value change of at least 8 degrees variance OR the air temperature value throws an I flag and the value change of air temperature from the previous is less than 8 degrees but more than six degrees, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing. 

Given the above, the following conjectures can be made:
* flags will not be synced amongst the attributes when a single M is thrown.
* flags will not be synced amongst the attributes when the VIM or VM codes are thrown (since they represent a single M).

Therefore, it is most important to find the conditions of single "M" as these indicate when the derived attribute isn't present.

### CENMET(2014):

|| 150 M ||
|:--|:----|:--:|
| **Attribute** | **How many of each flag** | ** Total Flags **|
| Air Temperature |'MM':11,'VI':3,'V':5 | 19 |
| Relative Humidity | 'MM':10, 'VI': 1, 'M':5, 'VM':4, 'VIM':2, 'V':1 |  23 |
| Dew Point | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure Defecit | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure | 'MM':11, 'VI', 'M':1, 'VM':5, 'VIM':2, 'V':1  | 24 |

For example, here is the hour surrounding the 'V' flagged temperature values from METDAT (started on 2014-08-26). **Note:** The whole week from 2014-08-22 to 2014-08-26 is oddly behaved; also, SAT VP is not DEW PT, but they are related.

|TmStamp | AirT[C] | VAP[mb]| SATVP[mb] | DEWPT[C] | RH[%] |
|-|-|-|-|-|-|
| 14:05:00 | NULL | NULL | NULL |	NULL | NULL |
|14:10:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
|14:15:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
|14:20:00 |	-76.48 | -0.494	| 2.051 | 2.544	| -34.33 |
|14:25:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
|14:30:00 |	19.6 |	16.36 |	25.82 |	9.46 |	59.18 |
|14:35:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
|14:40:00 |	-49.51 | 0.007 |0.134 |	0.127 |	-8.73 |
|14:45:00 |	-22.76 | 0.234 | 1.124 | 0.89 |	17.53 |
|14:50:00 |	-12.18 | 0.682 | 2.425 | 1.743 |27.94 |
|14:55:00 |	-13.36 | 0.759 | 2.495 | 1.736 | 26.71 |

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

Additionally, the 'VI' flag for Air Temperature at this height gets three hits on 2014-08-27. ** Note: ** Based on the conditions of the flag value change, we can assume that the 'VI' here is receiving the 'I' from an impossible jump in value, rather than from an impossible starting value. Whether or not one calls a -15 degree August morning impossible, which it is "not" in this case, is fair grabs.

| Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] |
|-|-|-|-|-|
| 08:20 | -11.060 | no flag | 28.810 | no flag |
| 08:25 | -15.116 | no flag | 24.880 | no flag |
| 08:30 | -15.440 | no flag | 24.540 | no flag |
| 08:35 | -5.403 | 'VI' |  nan | 'VIM' |
| 08:40 | 4.633 | 'VI' |  nan | 'VIM' |
| 08:45 | 14.67 | 'VI' | 87.2 | no flag |
| 08:50 | 14.730 | no flag | 87.5 | no flag |

Additional flags on relative humidity are accounted for by four missing values on 2014-08-26 on the relative humidity sensor ('M' code), as well as one missing value on the air temperature sensor on 2014-08-22 ('M' code from the air temperature sensor carried over). The other attributes appropriately reflect the combination of air temperature and relative humidity flags.

It is key to note that the times before August 27th on the CENMET Air Temperature are highly suspect, but are not flagged in the portal. It is also important to note the discrepancies between METDAT and Portal, particularly on 2014-08-26 at about 14:00

|| 450 M ||
|:--|:----|:--:|
| **Attribute** | **How many of each flag** | ** Total Flags **|
| Air Temperature |'MM':16,'VI':6,'Q':72 | 94 |
| Relative Humidity | 'MM':16, 'VI': 2, 'M':6865, 'VIM':4, 'Q': 71 | 6959 |
| Dew Point | 'MM':16, 'VI':2, 'M':6865, 'VIM':4, 'Q': 71 | 6959 |
| Vapor Pressure Defecit | 'MM':16, 'VI':2, 'M':6865, 'VIM':4, 'Q': 71  | 6959 |
| Vapor Pressure | 'MM':16, 'VI':2, 'M':6865, 'VIM':4, 'Q': 71 | 6959 |

The missing values of air temperature ('MM') correspond with 'MM' missing values in relative humidity, and these propogate to dew point, vapor pressure deficit, and vapor pressure.

Here is the hour in METDAT which contains many of the 16 'MM' flags for Air Temperature. It is the same hour, and day, as was called at the 150 m height.

|TmStamp | AirT[C] | VAP[mb]| SATVP[mb] | DEWPT[C] | RH[%] |
|-|-|-|-|-|-|
| 13:55:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:00:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:05:00 | -82.7 |	1.573 |	0.874 |	NULL |	-40.98 |
| 14:10:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:15:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:20:00 |	-59.64 |	0.799 |	2.133 |	NULL |	-18.75 |
| 14:25:00 |	-11.56 |	3.869 |	9.34 |	NULL |	28.48 |
| 14:30:00 |	-36.71 |	0.692 |	1.01 |	NULL |	3.768 |
| 14:35:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:40:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:45:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:50:00 |	NULL |	NULL |	NULL |	NULL |	NULL |
| 14:55:00 | NULL |	NULL |	NULL |	NULL |	NULL |

And here is that same hour in the Portal. 

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

While several values have been removed from portal that are likely to be "I", they are marked as "MM" despite having values in the data-stream. Based on this output, there is (currently) not a way to distinguish from impossible but extant values and missing values on the Portal, since the "I" flag is not even thrown on these odd returns.

Of particular interest is that the value at 14:25, which appears to have a reasonable relative humidity value of 28.48, and even the subsequent value of 3.768, has been removed from the Portal stram and appears as nan.

There are three values on 2014-08-22 also missing from air temperature on the portal. They have corresponding missing values for relative humidity on the Portal, and in both cases are flagged 'MM'. However, these values are existant (although not likely reasonable) in METDAT for air temperature, and possible reasonable for relative humidity in METDAT.

Here are the values on the Portal:

|Time | AirT[C] | flags on AirT[C] | RH[%] | flags on RH[%] |
|-|-|-|-|-|
|10:45:00 | nan | MM | nan | MM |
|10:50:00 | nan | MM | nan | MM |
|10:55:00 | nan | MM | nan | MM |

And their corresponding values in METDAT:

| TmStamp |	AirT[C]  |	VAP[mb] | SATVP[mb]| DEWPT[C] | RH[%] |
|-|-|-|-|-|
| 10:45:00| -37.42|	0.242 |	0.248 |	-69.69 | 2.357| 
| 10:50:00 |-28.75|	0.528 |	0.596 |	-50.74 | 10.5 |
| 10:55:00| -20.47|	0.991 |	1.215 |	-38.55 | 18.23| 

The six values flagged as VI on Portal are flagged consistently with the value in the relative humidity column, BUT the values on the Portal and those in METDAT are not the same. These values are from 2014-08-26.

|Time | AirT(MET) | RH(MET) | AirT(Portal) | RH(Portal)| 
|-|-|-|-|-|
|15:00:00 |	38.85 |	78.03 | 38.850 | 78.039 |
|15:05:00 |	18.1 |	57.64 |28.538 |nan  |
|15:10:00 |	6.576 |	46.31 |18.226 |nan  |
|15:15:00 |	7.914 |	47.65 | 7.914 | 47.650 |

The values of relative humidity that are "nan" in PORTAL have the additional "M" associated with being missing, so they are "VIM" (therefore the 6 'VI' from air temperature become 2 'VI' and 4 'VIM'). The second day of this trend is on 2014-08-27:

|Time | AirT(MET) | RH(MET) | AirT(Portal) | RH(Portal)| 
|-|-|-|-|-|
|08:40:00 |7.184 |60.83|-8.297 |nan |
|08:45:00 |16.77 |64.03| 4.447 |nan |
|08:50:00 |17.19 |61.3 |17.19 |61.3 |

Again, the problem of disagreement between the numbers on METDAT and on Portal appears. The Portal temperatures in this case have the "VI" (change in subsequent air temperature values of more than 8 degrees)  which propogates into the RH value, were it to be present, but the METDAT values do not agree, and seem realistic on both the air temperature and relative humidity values.

The 72 questionable values of air temperature on CENMET at 450 m are addressed here: [Questionable values](#qvals).

The nearly 7000 missing relative humidity values on CENMET are for the most part correlated with those on the Portal, except for on 2014-08-27 09:55:00 where there is 'NaN' on Portal, but a value of 34.31 in the database. The temperature values are the same.

### CENMET (2015):

No values for air temperature, dew point, relative humidity, vapor pressure defecit, or vapor pressure are flagged in 2015.

### VANMET (2014):

### VANMET (2015):

## Wintertime removals not reflected on all attributes<a id="nanlink"></a>

Air temperature sensors were removed for the winter at high elevation sites yet data was still included in the data stream and much of it were not flagged. Whenever sensors are removed, values should be set to NULL (SQL: NULL, MATLAB: NaN, Python: None) and flagged missing. Whenever sensors are removed, values should be set to NULL and flagged missing. The calculated dew point and vapor pressure deficit values were also erroneous for this period and not set to null or flagged missing. Suggest an automatic detection for removed sensors be established.

## Questionable values with no clear rationale<a id="qvals"></a>

Many values are flagged ‘Q’ with no other explanation.

### On Cenmet (2014):

The 450 m air temperature generates 72 "questionable" ('Q') values. Graphing these values reveals that they are indeed within the range of values that we would consider to be 'Q' based on the flags, and all precede the 2014-08-27 jump of the CENMET air temperature sensor to a more reasonable stream. Given the oddness of this part of the data stream in general, we suggest that these values all be flagged consistently. 

The additional 'Q's are associated with the missing relative humidity measurements on the same sensor. The 'Q' is carried along to make a 'QM'.

## Step Test for 'V' flags<a id="vvalsday"></a>

A step test looks for jumps in values based on a running mean and jumps are flagged as “v” in the hi-res data. The jump is be set for 6.5 degrees air temperature, which is probably ok for 5 or 15 minute data but falsely flag many values in hourly and daily data stream. These “v” flagged daily values are actually removed from the data stream in daily data sets and most of these are actually good values. Suggest not removing these “v”-flagged values or not running this algorithm on daily timestep data.

## Missing Times<a id="misstime"></a>

There are time gaps in data streams for several hours. These seem to occur when program changes are made, i.e., VANMET 09-13-2013. Suggest gap filling null values with missing codes.

### CENMET:

* CENMET 225 logger 2014 range: 16-May-2012 to 31-Dec-2014
    * 5 min (precip, snowdepth, etc.), missing values between 2012-12-21 15:55:00 and 2012-12-26 12:15:00; 
    * 15 min (airtemp and solar), missing dates: 2014-08-26 11:00:00 2014 to 2014-08-26 13:45:00 (inclusive), hourly appears to have all datetimes okay but is also split into the 225 file for 2015 (see below)
* CENMET 225 logger, 2015 range: 11-Dec-2014 to 03-Jan-2015,
    * 5 min (precip, snowdepth, etc.) all datetimes are okay,
    * 15 min (just solar), all datetimes are okay,
    * hourly - file is mapped to the 16-May-2012 to 31-Dec-2014 study period, does not relate
* CENMET 233 logger, part a, 2014 range: 22-Aug-2014 to 31-Dec-2014
    * 5 min (airtemp, dewpoint, soiltemp), all datetimes are okay 
    * hourly, all datetimes are okay
    * daily, all datetimes are okay
* CENMET 233 logger, part a, 2015 range: 12-Dec-2014 to 28-Jan-2015
    *  5 min(airtemp, relhum, wind, etc.), all datetimes are okay
    * hourly, all datetimes are okay
    * daily, all datetimes are okay

* overlap on CENMET 225 from 12 December to 31 December 2014
* overlap on CENMET 233 part a from 12 December to 31 December 2014
* CENMET hourly files for logger 225 are split by attribute from the 2012-2014 time period with replication of the soil attributes in both to the 2014 and 2015 "hourly" locations. as of 01-30-2015, I have reported this to Adam, as I assume it is a simple mistake that can be fixed. 
* **Note**: column organization on CENMET 233 hourly data has a 6 column date structure rather than the date structure reflected in other data sets

### VANMET:

All data prior to September of 2014 has been removed from the Portal, so missing date-times cannot be validated against what was previously found. Current status is as follows:

* VANMET 231 logger, 2014 range: 18-Sep-2013 to 31-Dec-2014
    * 5 min, hourly, daily (airtemp, etc.)  all datetimes are okay
* VANMET 231 logger 2015 range: 12-Dec-2014 to 30-Jan-2015 (current)
    * 5 min, hourly, daily (airtemp, etc.)  all datetimes are okay
* VANMET 232 logger 2014 range: 12-Sep-2013 to 31-Dec-2014
    * 5 min, hourly, daily (snow water, etc. in part 'a', wind in part 'b') , all datetimes are okay, 
* VANMET 232 logger 2015 range: 11-Dec-2014 - 30-Jan-2015 
    * 5 min, hourly, daily (snow water, in part 'a', wind in part 'b')(current) all datetimes are okay

* VARAMET 301, part a, range 2014: 21-May-2012 to 24-Dec-2014, 5 min (precip, snow depth, snow water e) 
    * 5 minute missing between:
        * 2012-12-21 15:55:00 and 2012-12-26 12:00:00 (records also missing in METDAT; missing values show round-off error on PORTAL: 2012-12-21 15:54:59, etc.)
        * 2013-07-18 20:50:00 and 2013-07-19 00:15:00 (missing also in METDAT, values show round off error on Portal, 2013-07-18 20:54:59)
        * 2014-09-21 07:40:00 and 2014-09-22 02:15:00, (missing also in METDAT, preceded by a long strand of NaN'ed out data, values generated are incorrect, i.e. 2014-09-21 07:39:59)
        * and 2014-10-02 00:55:00 and 2014-10-09 08:25:00 (same issue, preceded by NaN, also missing in METDAT, Portal displays rounding errors)
        
* VARAMET 301, part a, range 2015: 12-Dec-2014 to 30-Jan-2015 (current), 5min (precip, snow depth, snow water e) 
    * 5 minute missing 2014-12-24 13:25:00 through 2014-12-29 11:40:00
* VARAMET 301, part b, range 2014: 21-May-2012 to 24-Dec-2014, 15 min (only contains air temperature at 450) ; all date times are okay
* VARAMET 301, part b, range 2015: 12-Dec-2014 to 30-Jan-2015 (current), 15min (only contains air temperature at 450); all date times are okay

* overlap on VANMET 231 from 12-Dec-2014 to 31-Dec-2014
* overlap on VANMET 232 from 11-Dec-2014 to 31-Dec-2014. 
* missing chunk of data from VARAMET between 24-Dec 2014 and 29-Dec-2014, date stamps are present but data is NaN and stamps are off due to rounding.
* some values register in the inlocs table, see [Appendix1](#app1) 

### PRIMET:

* PRIMET 226 logger 2013: 
    * 5 min (SWE, etc.) missing dates between 2012-05-15 12:00:00 and 2012-05-15 12:45:00, 2012-11-25 20:55:00 and 2012-11-26 13:35:00, and 2012-12-21 15:55:00 and 2012-12-26 13:15:00
    * 15 minute logger(airtemp, solar), all datetimes are okay
    * hourly (soil and vpd), all datetimes are okay
* PRIMET 226, part a, 2014 range: 29-Apr-2013 to 31-Dec-2014
    * 5 min (airtemp, relhum, etc.), all datetimes are okay
    * hourly (airtemp, relhum, etc.), all datetimes are okay
    * daily all datetimes are okay
* PRIMET 226 logger, part a, 2015 range: 19-Dec-2014 to 30-Jan-2015 (current)
    * 5 min (airtemp, snow depth, wind), all datetimes are okay
    * hourly all datetimes are okay
    * daily all datetimes are okay
* PRIMET 229 logger, part a, 2014 range: 2014 16-Apr-2013 to 31-Dec-2014
    * 5 min (airtemp and solar) -- values incur round-off error between: 2013-08-19 22:45:00 (written as 2013-08-19 22:44:59) and 2013-08-22 10:45:00 (written as 2013-08-22 10:49:59). During much of this missing period, all data is recorded as NaN.
    * hourly (most attributes other than wind) all datetimes are okay
    * daily all datetimes are okay
* PRIMET 229 logger, part a, 2015 range: 19-Dec-2014 to 30-Jan-2015 (current)
    * 5 min (airtemp and solar), all datetimes are okay
    * hourly (most attributes other than wind) all datetimes are okay
    * daily all datetimes are okay
* PRIMET 229 logger, part b, range: 2014, 16-Apr-2013 to 31-Dec-2014
    * 5 min (wind and sonic), values incur round-off error between: 2013-08-19 22:45:00 (written as 2013-08-19 22:44:59) and 2013-08-22 10:45:00 (written as 2013-08-22 10:49:59). During much of this missing period, all data is recorded as NaN.
    * hourly (wind and sonic wind), all datetimes are okay
    * daily all datetimes are okay
* PRIMET 229 logger, part b, 2015 range: 19-Dec-2014 to 30-Jan-2015 (current)
    * 5 min (wind and sonic wind) all datetimes are okay
    * hourly (wind and sonic wind), all datetimes are okay
    * daily all datetimes are okay
* PRIMET 230 logger, part a, 2014 range: 02-May-2013 to 31-Dec-2014,
    * 5 min (soil, atm, etc.) all datetimes are okay
    * hourly(soil, atm, etc.), all datetimes are okay
    * daily all datetimes are okay
* PRIMET 230 logger, part a, 2015 range: 19-Dec-2014 to 30-Jan-2015,
    * 5 min (soil,atm., etc.) all datetimes are okay
    * hourly(soil, atm., etc), all datetimes are okay
    * daily all datetimes are okay

* PRIMET 226 logger overlap 29 Apr - 02 May 2013
* PRIMET 226 part a logger overlap 19 Dec - 31 Dec 2014
* PRIMET 229 part a logger overlap 19 Dec - 31 Dec 2014
* PRIMET 229 part b logger overlap 19 Dec - 31 Dec 2014
* PRIMET 230 part a (no part b) logger overlap, 19 Dec- 31 Dec 2014 
* Round off errors on all 229 logger parts in August 2013. Correspond to large chunks of all NaN data.
* Missing values from 5 minute data from three periods on the 2013 logger.

### H15MET:

* H15MET 207, 5 minute 2013 range: 01-Jan-2013 to 31-Dec-2013, daily range 02-Jan-2013 to 31-Dec-2013 - all datetimes are okay
* H15MET 208, 15 minute 2013 range : 31-Jan-2013 to 31-Dec-2013, daily range 01-Feb-2013 to 31-Dec-2013 - all datetimes are okay

* **Note: ** the date stamps on H15met are still formated as date-
### UPLMET:

* UPLMET 227 logger 2014 range: 29-May-2012 to 28-Dec-2014
    * 5 minute (snow, precip, etc.). Missing data between 2012-07-30 12:55:00 and 2012-07-31 15:30:0 caused by round off errors? (2012-07-30 12:59:59 is displayed, for example). The missing period is also missing in METDAT (here is the TmStamp, Year, Julian date, and hhmm columns from UPL_227_105.
    
            2012-07-30 06:55:00	2012 212 655
            2012-07-31 15:35:00 2012 213 1535	

    * between 2012-12-21 15:55:00 and 2012-12-26 12:20:00, in the backup table UPLO227\__inlocs\__ just preceding this period, the TmStamp does not appear to be registering on the 5 minute: 
            2012-12-21 10:03:52 is the entry in __inlocs__
            2012-12-21 10:00:00 is the entry in UPLO_227_105
            
    * and between 2014-09-13 17:30:00 and 2014-09-14 07:50:00. Once again the Portal values have round-off error, such as 2014-09-13  17:29:59, which persists to the end of the missing period. Neither \__inlocs\__ or UPLO_227_105 records any values.
    
    * 15 minute (airT, solar, atm pressure), all datetimes are okay. Even during the times when the five minute data is not recording at all, those 5 minute values are coming in on the 15 minute tables just fine.
    * all hourly and daily values are okay
    
* UPLMET 227 logger 2015 range: 11-Dec-2014 to 31-Dec-2014
    * 5 minute (snow, precip, etc.) all date times are okay
    * 15 minute (airT, solar, atm pressure) all date times are okay
    * all hourly and daily values are okay
    
### CS2MET:

## Coupled Q values<a id="coupleQ"></a>

Suggest follow-up be made for all “Q”-flagged values. The best recourse might be a comparison with other nearby same-site sensors or other sites. For example, valid temperatures of minus 15 to minus 17 occurred at all stations Dec 2013, but were flagged “Q”. These “Q” flags should be removed and possibly flagged as “verified as correct”.

### CENMET (2014)

Air Temperature has 72 Q values flagged for the 450 m sensor, but no Q values flagged for the 150 m sensor. Both sensors display very abnormally "low" values of air temperature for an early August time. Flags should match. 

## Appendix1<a id="app1"></a>

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

        TmStamp	RecNum	LOGGERID	PROGID	Year_RTM	Day_RTM	Hour_Minute_RTMPRECIP	OR_TEMP	SNOWDEPTH	QUALITY	SWE_AVG

What's odd here is the lack of consistency; I see pattern of having the date-value get 'off' by one second in the Portal and the data disappearing in METDAT synchonously somtimes, so I originally hypothesized that when values stop coming in, the GCE would gap fill in what is missing, but due to the glitch in MATLAB datetime objects is getting a rounding error. But on other sites, like this VARAMET, the data disappears from METDAT at least a full hour earlier than the date-number gets "off" on the Portal. And on the opposite extreme, the majority behavior is as expected: the data is missing, flagged as such, marked as NaN, and also METDAT has a full stream of NULL values. 

If we look back to the prior hour on Portal,  the data behaves as we expect 

        "VARMET",2014-09-21 06:00:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:05:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:10:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:15:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"
        "VARMET",2014-09-21 06:20:00,NaN,301,35.0,NaN,"M",NaN,"",NaN,"",NaN,NaN,"",NaN,"",NaN,"M"

In this set, the 4th column from the right end should be "snow depth." It is NaN. In METDAT, it is not there, so it is NULL. But if I open the table VAN_228__inlocs__, I see exactly one record in that 3 hour interval between 6 and 9 am on that day, which is: 

        TmStamp	RecNum	PRECIP	PUMPVOLTS	AIR_450	RAW_DIST	SWE	BATTERY_V	TKELVIN	REF_TEMP	MULT1	DISTTOSNW	DISTTOGND	SNOWDEPTH	OR_TEMP	CON_TEMP	RUN_TIME	LOGGERID	PROGID	QUALITY

        2014-09-21 06:18:47.8000000	33	39.45435	12.87784	18.4769-0.4315314	12.33467	291.6269	273.15	1.033268	0	5.6	5.6	17.4444	4	900	301	35	0


So, some measurement is being recorded for "snow depth" and if I am counting right it is "5.6" in this case. But that is the only measurement in that window. I "googled" \__inlocs_\_ to try to understand their role in logger-net and it seems like this table is generated "whenever the logger is checked for data"-- what that means, I do not really know. But it also doesn't seem to be very consistent, for example, when the data is missing from 2012-12-21 15:25 to 2012-12-26, the last entry in \__inlocs_\_ is at 10:04 am and it doesn't register again until 13:45 on 2013-01-02.

In short, it seems like there is a system error here, but I don't know what it is!
