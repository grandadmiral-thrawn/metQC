---
layout: post
title: "Missing Enumeration"
date: 2015-02-08T16:11:30-08:00
---

The following is a list of times when there are gaps in the data streams displayed on the Portal, by logger. When dates are displayed but with round-off-error, this is also discussed.


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
    
            2012-07-30 06:55:00 2012 212 655
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