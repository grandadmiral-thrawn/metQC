---
layout: post
title: "Min_max_checks"
date: 2015-02-03T14:30:24-08:00
---

# Table of Contents
  * [The Problem](#qlink)
  * [The Approach](#approach)
  * [AIR TEMPERATURE Maximums](#atmax)
  * [RELATIVE HUMIDITY Maximums](#rhmax)
  * [DEW POINT Maximums](#DPmax)
  * [AIR TEMPERATURE Minimums](#ATmin)
  * [RELATIVE HUMIDITY Minimums](#RHmin)
  * [DEW POINT Minimums](#DPmin)
  * [Take Home Points](#takehome)
  * [Jump Right To Images](#images)

## The Problem<a id="qlink"></a>

Data collected in the past included the instantaneous minimum and maximums of air temperature, relative humidity, solar radiation, and wind speed and direction (only maximum for wind) on a single day. This information is no longer being collected. Recently, we have used the five- or fifteen- minute minimum or maximum from the day to approximate these instantaneous values. But what do we lose if we choose to not capture these values?

Example (hypothetical):

* Instantaneous maximum is "37.89" and occurs at 12:34:05
* Five- minute preceding temperature is "36.35" at 12:30:00 and following is "35.87" at 12:35:00. 


## The Approach<a id="approach"></a>

## Data Extent for Air Temperature and Relative Humidity (and by derivation, dew point and vapor pressure defecit) <a id= "statlink"></a>

The table below describes the extent of the data used in this analysis.  The DAYS SHARED attribute is the number of days I used during which both five- and daily- data acquisitions appeared to be operational. During these times there were no long "streaks" of values gathered labelled as "NULL" and the values fell within an earthly range, here defined at greater than -50 C or less than 50 C for any air temperature. The LAST GATHERED attribute is the last day from which I collected data. There may be a few days of good data following this date.

| STATION | HEIGHT | DAYS SHARED | FIRST SHARED | LAST GATHERED |
|------|------|------|------|------|
| CENMET | 150 | 160 | 2014-08-29 | 2015-01-28 |
| CENMET | 250 | 160 | 2014-08-29 | 2015-01-28 |
| CENMET | 350 | 160 | 2014-08-29 | 2015-01-28 |
| CENMET | 450 | 160 | 2014-08-28 | 2015-01-28 |
| PRIMET | 150 | 267| 2014-05-13 | 2015-02-03 |
| PRIMET | 250 | 267| 2014-05-13 | 2015-02-03 |
| PRIMET | 350 | 267| 2014-05-13 | 2015-02-03 |
| PRIMET | 450 | 267| 2014-05-13 | 2015-02-03 |
| VANMET | 150 | 260| 2014-05-19 | 2015-02-03 |
| VANMET | 250 | 260| 2014-05-19 | 2015-02-03 |
| VANMET | 350 | 260| 2014-05-19 | 2015-02-03 |
| VANMET | 450 | 260| 2014-05-19 | 2015-02-03 |

The tables that follow describe results generated for a few stations. 
I did not address here the aspirated sensors for air temperature. After bring in, merging, and [filtering outliers](#outliers), I computed a basic set of metrics, and fed them into histograms to create probability distributions to exemplify and compare the behaviors of each set.

  * date-time for the daily date
  * maximums on the daily
  * minimums on the daily
  * maximums on the five minutes (max of five minute means for a day)
  * minimums on the five minutes (min of five minute means for a day)
  * difference between corresponding daily and five minute maxes (absolute value difference)
  * difference between corresponding daily and five minute minimums (absolute value difference)
  * percent of difference between the daily max and the daily mean 
  * percent of difference between the max of the five minute means for the day and the mean of five minute means for the day
  * percent of difference between the daily min and the daily mean
  * percent of difference between the minimum of the daily five minute means and the daily mean


<a id="outliers"></a> When generating histograms, I used 5 evenly spaced bins. In some cases, one or two values which were clearly erroneous for either of the two data sets were removed as they greatly skewed the distribution. When this removal fell well into the realm of impossibility, I noted the date and value and then removed it. When it was potentially questionable, I noted it for further exploration (see the [PRIMET maximums](#atmax) for an example).

Additionally, I independently validated 3 randomly selected days by randomly selecting a row using a random number generator between the collected data and the daily data being reported on the Portal. I also checked that the times of minimum and times of maximums reported on Portal for the five minute observation were the same as the ones that encompassed the maximum (or minimum) daily variables taken from instantaneous measurements daily temperature come from METDAT off of the daily (440) table. The key problem I found in this was that observations between 23:55 PM and Midnight could get assigned to the wrong time stamp, due to the timing discrepancy between the 2400 as midnight method versus the 0000 as midnight method. Although I initially thought I had found an example of this, I was incorrect; however, it did open my eyes to the fact that this error could exist, and would result in the daily minimum or maximum value being cast to the prior day, should it not be taken using the daily synopsis technique. In short, this is an inconsistency between the two methods that will not be resolved unless the TmStamp is reformated in either the newer or older data sets. 

* ** Note: ** When calculating the average difference between the daily mean value and the daily max or min value, I used the median rather than the statistical mean, as often one outlier that I could not immediately determine if real or incorrect would skew the distribution too much. 

AIR TEMPERATURE MAXIMUMS <a id = "atmax"></a>
----------------

Here are a few examples of air temperature maximums, collected from the four sensors on CENMET:

At the 150 m height, AIRCEN01:

* ** Overview: ** 153 values collected

* ** Maximum difference ** 0.51 C on 2014-09-09

* The daily maximum temperatures are on average 70.71 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 68.6 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures


* Tables like this contain the boundaries of the grouping bins in a histogram, the count of the values encompassed by that bin, and the percent of the total values in that bin. The below would be read as "forty-four percent of all differences between the daily measurement of maximum temperature and the maximum of the five minute mean fell within a window of less than 0.1 degrees C"

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1  | 71 | 44 |
| 0.1 to 0.2 | 63 | 39 |
| 0.2 to 0.3 | 20 | 13 |
| 0.3 to 0.4 | 5 | 3 |
| > 0.5  | 1 | 1 | 



Validations conducted on air temperature at CENMET 150m on 2014-10-29, 2014-10-07, 2014-11-24.

* Tables like this contain the date being validated, the maximum value for the day on Portal, the maximum value for the day in METDAT, etc. with PORT being "Portal" and MET being "METDAT"

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-10-29 | 14.51 | 14.51 | 13:30 | 13:29 | 6.047 | 6.047 | 7:13 | 7:15 |
|2014-10-07 | 30.19 | 30.19 | 14:40 | 14:37 | 12.00 | 12.03 | 6:35 | 6:33 |
|2014-11-24 | 9.13  | 9.13  | 13:25 | 13:24 | 1.04 | 1.04 | 6:24 | 6:25 |


( The reported values are in sync with those in the database)

At the 250 m height, AIRCEN02 reports:

* ** Overview: ** 160 values collected

* ** Maximum difference ** 0.69 C on 2014-11-26
            
* The daily maximum temperatures are on average 67.11 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 64.11 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures


| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1  | 65 | 41 |
| 0.13 to 0.27 | 71 | 44 |
| 0.27 to 0.41 | 20 | 13 |
| 0.41 to 0.55 | 5 | 2 |
| > 0.55 | 1 | 1 |

Validations were conducted for 2014-09-02, 2014-11-07, and 2014-12-06

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-09-02 | 22.77 | 22.77 | 14:00 | 13:55 | 7.089 | 7.089 | 23:55 | 00:00 |
|2014-11-07 | 13.66 | 13.66 | 15:30 | 15:30 | 1.813 | 1.813 | 7:20 | 07:18 |
|2014-12-06 | 7.442  | 7.442  | 11:20 | 11:16 | 1.851 | 1.851 | 22:00 | 21:59 |

(The reported values are in sync with those in the database)


At 350 m height, AIRCEN03 reports: 

* ** Overview: ** 160 values collected

* ** Maximum difference ** 1.32 on 2014-11-26
    
* The daily maximum temperatures are on average 63.63 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 61.41 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures


| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.2 | 128 | 78 |
| 0.2 to 0.5 | 33 | 21 |
| 0.5 to 0.8 | 1 | 1 |
| 0.8 to 1.1 | 0 | 0 |
| > 1.1 | 1 | 1 |


Validations were conducted for 2014-10-16, 2014-12-13, and 2014-09-28

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-10-16 | 16.530 | 16.53 | 14:30 | 14:27 | 4.248 | 4.248 | 02:10 | 01:57 |
|2014-12-13 | 6.312 | 6.416 | 12:25 | 12:25 | -0.765 | -0.765 | 20:40 |20:37 |
|2014-09-28 | 22.46  | 22.46  | 14:45 | 14:45 | 7.717 | 7.717 | 01:45 | 01:45 |
 
* The Portal five minute value and the database five minute value for the minimum are in sync, but this actual minimum value on 2014-10-16 was about three-one-hundreths of a degree colder and occured about 15 minutes earlier, as 4.218 at 01:57. 


The graph below shows the distribution of the air temperature maximums on CENMET at 350 m height

<iframe src= "http://bl.ocks.org/dataRonin/83465daf2ee7fe16255c" width="650" height="600" scrolling="no"></iframe>



At 450 m height, AIRCEN04 reports:

* ** Overview: ** 160 values collected

* ** Maximum difference ** 4.51 C, 2014-11-06
    
    * In this case the maximum value was 19.54 C on the daily measurement and the minimum value was 15.24 C on the five minute measurement. Both datasets expressed similar daily means (8.38 C for the daily and 8.40 C for the five minute)
    * This value occurred at 10:54:54 am.

* The daily maximum temperatures are on average 69.17 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 67.47 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures


| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| 0.01 to 1.8| 158| 99 |
| 1.8 to 3.6 | 1 | 1 |
| 3.6 to 5.4 | 0 | 0 |
| 2.71 to 3.61 | 0 | 0 |
| > 3.61 | 1 | 1 |

Validations were conducted on 2014-08-30, 2014-12-09, and 2014-02-02

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-08-30 | 13.96 | 13.96 | 11:40 | 11:36 | 9.55 | 9.55 | 23:45 | 23:43 |
|2014-12-09 |11.170 | 11.417 | 10:20 | 10:17 | 6.331 | 6.331 | 06:25 |06:38 |
|2014-02-02 | 7.536  | 7.536  | 14:40 | 14:38 |1.516 | 1.516 | 22:20 | 22:13 |

** Note about time difference **

On the December 9th value, it appears that the minimums observed by Portal and the minimum of the five minutes are about fifteen minutes earlier than the actual daily minimum, which was 6.295. This is within a tenth of a degree of the five minute minimum, however.


On PRIMET, similar trends were observed. Here I will also showcase a few outliers that affect the distributions prior to their removal.

* ** Overview: ** 266/267 values collected at 150 m

* ** Maximum difference ** 9.158 on 2014-11-12, after removal 0.51 on 2014-01-18

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-11-12 00:00:00 | PRIM_226_table105 | 8.24 | PRIM_226_table440 |-0.918| 

* The five-minute maximum on this day is 8.24, although both the daily mean and the five minute mean are consistent (0.798 C five minute versus -1.21 C daily, recalling that this outlier is also certainly pulling the daily mean)

* Days preceding this one show similar daily maximums to the five-minute value of 9 C, while days following this one show similar daily maximums to the daily value, between zero and two degrees. 

* Besides this outlier, all values were less than half of a degree of difference between methods.

* The daily maximum temperatures are on average 59 percent greater than the mean temperature for the day as calculated on the daily summary

* The five-minute maximum temperatures are on average 58 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures


| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.2 | 121 | 46 |
| 0.2 to 0.3 | 97 | 37 |
| 0.3 to 0.4 | 35 | 13 |
|0.4 to 0.5 | 11  | 0.4 |
| >0.5 | 2 | 1 |



Validations were conducted on 2014-12-29, 2014-11-14, 2014-07-04

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-12-29 | 2.60 | 2.60 | 14:10 | 14:10 | -4.732 | -4.68 | 23:45 | 23:58 |
|2014-12-09 |7.19 | 7.189 | 12:45 | 12:45 | -0.345 | -0.346 | 23:55 |23:58|
|2014-07-04 | 28.19  | 28.19  | 14:15 | 14:38 |10.84 | 10.84 | 04:30 | 04:26 |

** Note about time difference **

On the 2014-12-29 and 2014-07-04 measurements, the values are similar between the Portal and METDAT, but the time of the maximum differs.

On PRIMET at 250 m, AIRPRI02 reports:

* ** Overview: ** 266/267 values collected

* ** Maximum difference ** 8.838 on 2014-11-12, after removal of outlier, 0.68 is maximum difference which occurs on 2014-10-08.

** A NOTE ABOUT A POTENTIALLY PROBLEMATIC DAY AT PRIMET**

The data on 2014-11-11 is continuously suspect, here is the 250 example.It's removal reduces the maximum difference to less than a degree

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|    
| 2014-11-12 00:00:00 |PRIM_226_table105 | 8.48 | PRIM_226_table440 |-0.358 |

Likewise, this day is a problem at 350 m

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----| 
|2014-11-12 00:00:00 |PRIM_226_table105 |8.66 |PRIM_226_table440 |-0.199|

Maximum difference ** 8.859 on 2014-11-11, after removal it is 0.64

and at 450 m 

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----| 
|2014-11-12 00:00:00 |PRIM_226_table105 |8.66 |PRIM_226_table440 |-0.199|


* The daily maximum temperatures at 250, 350, and 450 m are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary

* The five-minute maximum temperatures are also on average 56 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures

* Besides the outlier, all values were less than one degree of difference between methods.

Validations were conducted on 2014-07-30, 2014-08-22, and 2014-12-07

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-07-30 | 33.96 | 33.96 | 13:50| 14:50 | 13.81 | 13.81 | 5:15| 5:17 |
|2014-08-22| 26.11 | 26.11| 12:45 | 12:45 | 9.18 | 9.18 | 23:55 |3:55|
|2014-12-07 | 9.33  | 9.33  | 14:40 | 14:38 |0.626 | 0.626 | 07:25 | 07:24|

On VANMET, similar trends were seen. A few more examples:

* The day of 2014-06-13 is a problematic day on the 150 m and 450 m sensors at VANMET; here at 150 m:

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
|2014-06-13 00:00:00|"Van_231_Table105"|"14.35"|"Van_231_Table440" |"18.63"|


and at 450 m:

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-06-13 00:00:00 |Van_231_Table105 | 12.94 |Van_231_Table440 |19.28|


Other than these days, the maximum differences on air temperature at VANMET were less than 0.68.  Maximum values were approximately 55 percent greater than the mean for both methods. 


---------

### although data was only available at a 15 minute resolution for H15MET and UPLMET, I went ahead and looked at this data to see if it also reflected similar trends.

Here is an image of the difference between daily maximums and 15 minute maximums on H15MET. ** THE OUTLIER DAY HAS NOT BEEN REMOVED PRIOR TO THE GENERATION OF THIS HISTOGRAM **

<iframe src= "http://bl.ocks.org/dataRonin/0f1988059058a28dc705" width="650" height="600" scrolling="no"></iframe>


At H15MET, the percent difference between the 15 minute daily temperatures as the maximum of the day versus the instantaneous maximum of the day showed that only one value had a difference of more than 0.2 degrees. This value came from the day 2013-02-01, and the daily instruction appears to be incorrect, showing a maximum value of 23.25 C (and a minimum value of -85 C).

The average difference between maximum and mean air temperature for a day was 51 percent for both methods at H15MET.

----------------

RELATIVE HUMIDITY MAXIMUMS <a id = "rhmax"></a>
----------------

Here are a few examples of relative humidity maximums, collected from several sensors:

At the 150 m height, RHCEN01:

* The maximum difference between five- minute relative humidity maximum and daily relative humidity maximum was 55.13 percent and occured on 2014-09-11.

* on this day, the daily measurement was 96.3 percent for the maximum while the five-minute measurement was only 40.3 percent. The value of 96.3 percent is more similar to the other measurements on this sensor during that week, which were also in the 90's. This value is also more similar to the measured values of 100.0 on PRIMET on this day at 150 m for the daily and 95.5 on this day for the five-minute.

* On average, the maximum relative humidity is only 8 percent greater than the mean for both the daily and five minute methods on CENMET 150 at 150 m. 

* After removing outliers, 91 percent of daily maximum values and maximum values for the day from five minute means are within 10 percent of one another. 

The graph below shows the distribution of maximums on VANMET 150 before the outliers are removed. ** Please be aware that the y-axis should be multiplied by 10 to get an appropriate probability.** I.e. prior to outlier removal, about 82 percent of maximum values were still between 0 and 10 percent relative humidity of one another. I am not sure why the histogramming function is generating this error, but it is internal and I will look into it. 

<iframe src= "http://bl.ocks.org/dataRonin/784c6890f5b9feea97ad" width="650" height="600" scrolling="no"></iframe>


Relative humidity maximums on CENMET 450 (a discussion):

* Comparing the 150 m and 450 m height, it is evident that when there is a large difference between the relative humidity maximum measured on the daily measurement versus the daily maximum as computed from the five minute means, this difference is often due to an error that is sensor specific. For example, the maximum difference between the two methods occurs on the CENMET relative humidity sensors on 2014-09-11. On this day, the daily measurement is 87.7 percent relative humidity whereas the five-minute measurement is 21 percent.

* Air temperature on this day were also problematic and removed from the data, and measurements of the difference in humidities on VANMET and PRIMET are more similar to the 87.7 percent. Furthermore, the rest of the week also has a relative humidity that is greater than 60 percent for daily measurements and five minute measurements.

* The average percent difference in relative humidity maximums from the mean relative humidity is 16 percent in both the five minute and daily methods.

Relative humidity maximums on PRIMET (a discussion):

* the 450 m sensor does not appear to be functional for a long duration of the time period.

* based on observations at 150 m, 
  * The greatest difference between the five-minute and instantaneous maximums was 12 % on 2014-09-12. On this day the daily value exceeded the 5 minute value at 95 percent versus 83 percent. 
  * 92 percent of differences between methods were less than 12 percent. 

Relative humidity maximums on VANMET (a discussion):

* on VANMET, the same 2014-09-11 emerges for having discrepancies between the five minute maximum and daily maximum values.

* However, the mean difference between the maximum and median relative humidity at VANMET is 20.5 degrees in the maximum values from daily and 20.4 in the version in the five minute data; this may be within acceptable tolerance.

* Only 67 percent of vanmets values are within 10 percent of the mean.




#### VANMET 450: DEWPOINT, DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY-MAX

* The maximum difference between the daily maximum from 5 minute values versus the instantaneous maximum was 18.9 degrees due to this erroneous value, 

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-11-08 00:00:00 | Van_231_Table105 | 9.3 |Van_231_Table440 |-9.6|

#### CENMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN

* ** Overview: ** 160 values collected
* ** Maximum difference ** (between minimums) 0.304 on 2014-10-01
    

* The daily minimum temperatures are on average 42.2 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 41.5 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1 | 139 | 87 |
| 0.1 to 0.2 | 14 | 9 |
| 0.2 to 0.3 | 1 | 1 |
|0.3 to 0.4 | 4  | 3 |
| 0.4 to 0.5 | 2 | 1 |

* validations are included in the maximums section

#### CENMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN

* ** Overview: ** 160 values collected
* ** Maximum difference ** (between minimums) 0.312 on 2014-10-01
    

* The daily minimum temperatures are on average 40.4 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 40.2 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.06 | 135 | 84 |
| 0.6 to 0.12 | 17 | 11 |
| 0.12 to 0.18 | 3 | 2 |
| 0.18 to 0.24 | 2  | 2 |
| >0.24 | 2 | 1 |

* validations are included in the maximums section

#### CENMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN

* ** Overview: ** 160 values collected
* ** Maximum difference ** (between minimums) 0.321 C on 2014-10-01
    

* The daily minimum temperatures are on average 39.88 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 32.9 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.06 | 135 | 84 |
| 0.6 to 0.12 | 17 | 11 |
| 0.12 to 0.18 | 3 | 2 |
| 0.18 to 0.24 | 2  | 2 |
| >0.24 | 2 | 1 |

* validations are included in the maximums section

#### CENMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN

* ** Overview: ** 160 values collected
* ** Maximum difference ** (between minimums) 0.257 on 2014-10-01
    

* The daily minimum temperatures are on average 40.4 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 40.2 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.05 | 136 | 89 |
| 0.05 to 0.1 | 15 | 4 |
| 0.1 to 0.15 | 6 | 3 |
| 0.2 to 0.25 | 1  | 3 |
| >0.25 | 2 | 1 |

* validations are included in the maximums section

#### PRIMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN for AIRTEMP and RELATIVE HUMIDITY.

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.25 C on 2014- 07-21.

* The daily minimum temperatures are on average 40.4 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures

* ** Note: ** the above "averages" are actually medians to remove outlier effect 

One outlier of note: 


| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-06-13 00:00:00 | PRIM_226_table105 | 8.55 | PRIM_226_table440 |-23.94 |


On the same day, the relative humidty also had a simiilar large difference in minimum values

* On average, the daily minimum relative humidities were about 30 percent less than the mean from both summary sets.
* On average, the daily maximum relative humidities were about 8 percent higher than the mean.
* 216 of the 260 values had a 100 percent maximum humidity. 
* 30 of the 260 values had a 100 percent minimum humidity for the day (indicating they were humid all day)


| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-06-13 00:00:00 | PRIM_226_table105 | 99.00 | PRIM_226_table440 |-25.3 |

Following removal of the outlier, the data behaved much more robustly; No minimum values on PRIMET's air temperature differ by more than 0.6 degrees at the 150 m height. 

* validations are included in the maximums section

#### PRIMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.21 C on 2014-07-21

* The daily minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.4 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 


No minimum values on PRIMET differ by more than 0.6 degrees at the 250 m height

* validations are included in the maximums section

#### PRIMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.19 C on 2014-07-21

* The daily minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.4 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* validations are included in the maximums section

#### PRIMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 265 / 267 values collected
* ** Maximum difference ** 0.15 C on 2014-06-25

    * I removed two major outliers in order to reduce the minimum difference from 32 degrees to less than one degree. Here are those points: 

    | DATE | Five Minute Table | Value | Daily Table | Value |
    |-----|-----|-----|-----|-----|
    | 2014-06-12| "PRIM_226_table105" | -7.875 | "PRIM_226_table440" |-43.01 |
    | 2014-01-28| "PRIM_226_table105" | 1.125 | "PRIM_226_Table440" | -31.16 |

* The daily minimum temperatures are on average 40.5 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.9 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* validations are included in the maximums section


#### VANMET 150: DIFFERENCES BETWEEN 5 MINUTE DAILY RELATIVE HUMIDITY, and DEWPOINT. 

Similar to the other stations, VANMET showed 

Before removing the largest outlier of 98 percent difference on 2014-06-13 (a day which was also problematic for PRIMET at 150m), VANMET's largest difference was expansive. However, even after removal the largest difference between the daily minimum relative humidity percent and the minimum percent from five minute intervals for the day is 67 percent relative humidity.

For the five-minute method, the difference between the five minute minimum relative humidity and the mean is approximately 37 , for the daily method, the difference is closer to 44 percent. 

An interesting test I looked at on this site was where the five minute minimum relative humidity was 100 %, was the daily minimum relative humidity also 100%? If it was, this might indicate persistance issues-- however, in all but three cases, on days where the five minute minimum is 100 percent, the daily minimum is actually much lower. Below, the dotted blue line is the minimum relative humidity daily course from the daily minimums, the blue squares are when the daily minimum is 100 percent humidity, and the red squares are when the five minute minimums are 100 percent. 

<iframe src= "http://bl.ocks.org/dataRonin/63d7f6595a57033dceb8" width="800" height="600" scrolling="no"></iframe>

In short this shows that the daily minimum may indeed be much lower than the five minute minimum relative humidity. 

The dewpoint on VANMET also showed strong discrepancy between the five minute values and the daily values. Since we see that the air temperature is relatively stable between these, suffice it that the relative humidity appears to drive the difference in dew points. Two 
values were removed:

* Found an erroneous minimum in the daily dataset of -72 dew point. 

| DATE | Five Minute Table | Value | Daily Table | Value |
    |-----|-----|-----|-----|-----|
| 2014-06-08 00:00:00 |Van_231_Table105| 5.781 |Van_231_Table440  |-72.32|

"2014-11-15 00:00:00","Van_231_Table105","-10.8888","-6.397","-17.28","Van_231_Table440","0.575","4.162","-6.625","2014-11-14 00:15:00","2014-11-14 23:59:30",10.559000000000001,10.655000000000001,-0.4125,6.2383,-0.587,12.5217


#### TAKE HOME POINTS for AIR TEMPERATURE:<a id="takehome"></a>

Given the consistency between the above results, I have developed some take-home points that may be useful for future flagging on AIR TEMPERATURE.

* maximums are about 65 percent greater than daily mean in both five minute and instantaneous methods
* minumums are about 40 percent less than daily mean in both five minute and instantaneous methods
* maximums are less stable than minimums (in general the variability on both is small at the sub five minute scale, but it is even less on minimums than maximums)
* all of the max daily temperatures from instantaneous are less than one and a half degrees off the five- minute values after a few spikes (described) were removed.
* the true daily maximum/minimum usually occurs within the same five minute interval as the five-minute maximum/minimum selected from the day, but not always

* it seems like the retention of the time of max and time of min is an important feature, but that the five minute data does seem to provide an adequate representation. 

* Reports in METDAT (table CENT_233_Table440) can e slightly different (due to rounding?) than those on Portal. I selected this day because on both it seems a little too high for a January so I was exploring it anyway.

    * 19.88, Jan. 26 2015 01:50:15:000PM
    * 20.22, Jan. 26 2015 01:43:30:000PM
    * 20.49, Jan. 26 2015 01:43:30:000PM
    * 20.27, Jan. 26 2015 01:43:30:000PM

* Portal Reports for cenmet_233_a_dly_2015.csv (these are the daily values):
 
    * at height 150: 19.700,"",13:55:00
    * at height 250, 20.070,"",13:50:00
    * at height 350, 20.360,"",13:45:00
    * at height 450, 20.140,"",13:45:00

* a simple check for maximum and minimum might be a QUESTIONABLE type flag for maximums that are more than 75% greater than the mean, or minimums that are more than 50% less than the mean. This should almost never occur, and it could be implemented in one cell of MATLAB as (theoretically):

        if (five_max - five_mean)/ five_mean > 0.7
            flag = "Q";
        else flag = "A";
        end