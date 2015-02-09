Checks on GCE_to_FSDB Document
-----------------------------

The purpose of this analysis is to review possible changes and fixes in the GCE output .csv files that may affect data quality in FSDB. My role was to review potential problems in the GCE output, see if those problems were fixed, and see if the fixes were propogating into future outputs. To do this I developed my own toolkit which replicated the graphical properties of GCE, and also allowed comparisons across datafields.

**Note:** Within this document I may use the terms "NULL", "NaN", and "None" interchangeably, to refer to data that does not have a value, but does have a type (such as "integer" or "string"). This is different from "empty" which might appear like this: '', ' ', "", " ", &nbsp, u'', U+00A0, etc...

How an "empty" is interpreted varies wildly, see [Wikipedia Article on WhiteSpace](http://en.wikipedia.org/wiki/Whitespace_character#Unicode) for more information. My goal here is just to point out that "empty" and "null" are NOT the same.

**Note:** Additionally, I tried to keep consistent naming and units when possible. AirT is Celcius air temperature, RH is relative humidity in percent, DEWPT is the dew point temperature in Celcius, VAP is the Vapor Pressure is the equilibrium vapor pressure in milli-bars (mb), SATVP is saturated vapor pressure in millibars, and VPD is the vapor pressure defecit, also in millibars. 

**Note:** These are only examples of the types of problems seen. Once a production environment has been set up that checks for these errors, we will conduct more extensive follow up. 

# Table of Contents
  * [Existing flag codes](#flagcodes)
  * [Synchronized Flags across AIRT, DEWPT, VPD, RELHUM and VAP](#symlink)
  * [Wintertime removals not reflected on all attributes](#nanlink)
  * [Questionable Values with no rationale](#qvals)


## Existing flag codes<a id = "flagcodes"></a>
Flag Codes, at 5 minutes. If a less stringent flag is caught within a more stringent flag, both flags will be displayed. 

* I: An air temperature is below - 35 deg C or above 50 deg C OR a subsequent value is at least 8 deg C above or below the preceding 5 minute value. This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes.
* MM : On air temperature the "M" flag for NaN is thrown twice, so in all cases, "MM" will appear rather than just "M". This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes. 
* VI : A subsequent air temperature value is at least 8 deg C above or below the preceding 5 minute value. Catches the "V" flag from this case. This flag is carried into the vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes.
* V : A subsequent air temperature value is at least 6.5 deg C above or below the preceding 5 minute value.
* M : Will never appear on air temperature alone in the current state (01-28-2015). Can appear in vapor pressure, dew point, vapor pressure defecit, and relative humidity attributes if they are uniquely missing, but air temperature is not.
* VM : The air temperature value throws a flag value change of at least 6.5 degrees variance, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing. 
* VIM : The air temperature value throws a flag value change of at least 8 degrees variance OR the air temperature value throws an I flag and the value change of air temperature from the previous is less than 8 degrees but more than six degrees, and the other attribute (vapor pressure, dew point, vapor pressure defecit, or relative humidity) is uniquely missing.
* IQVIQ :


## Synchronized Flags and NaN's across AIRT, DEWPT, VPD, RELHUM and VAP<a id="symlink"></a>

Air temperature, relative humidity, dew point, vapor pressure, vapor pressure defecit (VPD) are not synchronized. Quality or missing flags from air temperature and relative humidity should be passed along to the calculated dew point and VPD data.

Here are a few examples of flags, and their number, on CENMET, at the 150 m height:

### CENMET(2014), summary of flags:

|| 150 M ||
|:--|:----|:--:|
| **Attribute** | **How many of each flag** | ** Total Flags **|
| Air Temperature |'MM':11,'VI':3,'V':5 | 19 |
| Relative Humidity | 'MM':10, 'VI': 1, 'M':5, 'VM':4, 'VIM':2, 'V':1 |  23 |
| Dew Point | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure Defecit | 'MM':11, 'VI':1, 'M':5, 'VM':4, 'VIM':2, 'V':1  | 24 |
| Vapor Pressure | 'MM':11, 'VI', 'M':1, 'VM':5, 'VIM':2, 'V':1  | 24 |

### The very bad week of 2014-08-22 to 2014-08-26:

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

### When flag value change is thrown in a case that is better described by impossible value.

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


### When a missing flag on air temperature destroys other values and flags for that Date time, and those other values and flags represent likely impossible data.

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

Pay attention to the values between 14:20 and 14:30, where relative humidity, even when odd, does exist.  Here is that same hour on Portal.

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

### When a existing value on air temperature is deemed impossible and destroys existing and possible values on other attributes (again on CENMET):

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