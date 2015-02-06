---
layout: post
title: "Min_max_checks"
date: 2015-02-03T14:30:24-08:00
---

# Table of Contents
  * [The Problem](#qlink)
  * [The Approach](#approach)
  * [Basic Statistics for Air Temperature](#statlink)
  * [Take Home Points](#takehome)
  * [Jump Right To Images](#images)

## The Problem<a id="qlink"></a>

Data collected on METDAT of the instantaneous minimum and maximums of air temperature, solar, and wind for a single day is no longer being maintained. Recently, we have used the five- or fifteen- minute minimum or maximum from the day to approximate these instantaneous values. But what do we lose if we choose to not capture these values?

Example (hypothetical):

* Instantaneous maximum is "37.89" and occurs at 12:34:05
* Five- minute preceding temperature is "36.35" at 12:30:00 and following is "35.87" at 12:35:00. 


## The Approach<a id="approach"></a>

## Data Extent for Air Temperature<a id= "statlink"></a>

The table below describes the extent of the data used in this analysis.  The DAYS SHARED attribute is the number of days I used during which both five- and daily- data acquisitions appeared to be operational; values gathered were not labelled as "NULL" and within a reasonable range, here defined at greater than -50 C or less than 50 C for any air temperature. The LAST GATHERED attribute is the last day from which I collected data. There may be a few days of good data following this date.

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

The tables that follow describe histogrammed results generated for each station, each height, and each air temperature, but do not address the aspirated air temperature. The histograms were generated using 5 evenly spaced bins. In some cases, one or two values which were clearly erroneous for either of the two data sets were removed as they greatly skewed the distribution. When this removal fell well into the realm of impossibility, I noted the date and value and then removed it. When it was potentially questionable, I noted it for further exploration (see the [PRIMET maximums](#primetmax) ).

Additionally, I independently validated 3 randomly selected indices (which correspond to dates) of observations in several of the five minute data set versus what is being reported on the Portal. These indices were selected using a random number generator from 0 to the number of observations for each station. The times of minimum and times of maximum daily temperature come from METDAT off of the daily (440) table.

#### CENMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX FOR AIR TEMPERATURE

* ** Overview: ** 153 values collected
* ** Maximum difference ** 0.51 C on 2014-09-09

* The daily maximum temperatures are on average 70.71 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 68.6 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1  | 71 | 44 |
| 0.1 to 0.2 | 63 | 39 |
| 0.2 to 0.3 | 20 | 13 |
| 0.3 to 0.4 | 5 | 3 |
| > 0.5  | 1 | 1 |

Validations conducted on air temperature at CENMET 150m: 2014-10-29, 2014-10-07, 2014-11-24

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-10-29 | 14.51 | 14.51 | 13:30 | 13:29 | 6.047 | 6.047 | 7:13 | 7:15 |
|2014-10-07 | 30.19 | 30.19 | 14:40 | 14:37 | 12.00 | 12.03 | 6:35 | 6:33 |
|2014-11-24 | 9.13  | 9.13  | 13:25 | 13:24 | 1.04 | 1.04 | 6:24 | 6:25 |

The reported five minute values are in sync with those in the database.

#### CENMET 150: DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX FOR RELATIVE HUMIDITY

* The maximum difference between five- minute relative humidity maximum and daily relative humidity maximum was 55.13 percent and occured on 2014-09-11.
* on this day, the daily measurement was 96.3 percent for the maximum while the five-minute measurement was only 40.3 percent. The value of 96.3 percent is more similar to the other measurements on this sensor during that week, which were also in the 90's. This value is also more similar to the measured values of 100.0 on PRIMET on this day at 150 m for the daily and 95.5 on this day for the five-minute.
* On average, the maximum relative humidity is only 8 percent greater than the mean for both the daily and five minute methods on CENMET 150 at 150 m. 
* 91 percent of daily maximum values and maximum values for the day from five minute means are within 10 percent of one another. 

#### CENMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 160 values collected
* ** Maximum difference ** 0.69 C on 2014-11-26
            
* The daily maximum temperatures are on average 67.11 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 64.11 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1  | 65 | 41 |
| 0.13 to 0.27 | 71 | 44 |
| 0.27 to 0.41 | 20 | 13 |
| 0.41 to 0.55 | 5 | 2 |
| > 0.55 | 1 | 1 |

Validations: 2014-09-02, 2014-11-07, 2014-12-06

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-09-02 | 22.77 | 22.77 | 14:00 | 13:55 | 7.089 | 7.089 | 23:55 | 00:00 |
|2014-11-07 | 13.66 | 13.66 | 15:30 | 15:30 | 1.813 | 1.813 | 7:20 | 07:18 |
|2014-12-06 | 7.442  | 7.442  | 11:20 | 11:16 | 1.851 | 1.851 | 22:00 | 21:59 |

The reported five minute values are in sync with those in the database.

#### CENMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 160 values collected
* ** Maximum difference ** 1.32 on 2014-11-26
    
* The daily maximum temperatures are on average 63.63 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 61.41 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.2 | 128 | 78 |
| 0.2 to 0.5 | 33 | 21 |
| 0.5 to 0.8 | 1 | 1 |
| 0.8 to 1.1 | 0 | 0 |
| > 1.1 | 1 | 1 |


Validations: 2014-10-16, 2014-12-13, 2014-09-28

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-10-16 | 16.530 | 16.53 | 14:30 | 14:27 | 4.248 | 4.248 | 02:10 | 01:57 |
|2014-12-13 | 6.312 | 6.416 | 12:25 | 12:25 | -0.765 | -0.765 | 20:40 |20:37 |
|2014-09-28 | 22.46  | 22.46  | 14:45 | 14:45 | 7.717 | 7.717 | 01:45 | 01:45 |
 
* The Portal five minute value and the database five minute value for the minimum are in sync, but this actual minimum value on 2014-10-16 was about three-one-hundreths of a degree colder and occured about 15 minutes earlier, as 4.218 at 01:57. 

#### CENMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 160 values collected
* ** Maximum difference ** 4.51 C, 2014-11-06
    
    * In this case the maximum value was 19.54 C on the daily measurement and the minimum value was 15.24 C on the five minute measurement. Both datasets expressed similar daily means (8.38 C for the daily and 8.40 C for the five minute)
    * This value occurred at 10:54:54 am.

* The daily maximum temperatures are on average 69.17 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 67.47 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| 0.01 to 1.8| 158| 99 |
| 1.8 to 3.6 | 1 | 1 |
| 3.6 to 5.4 | 0 | 0 |
| 2.71 to 3.61 | 0 | 0 |
| > 3.61 | 1 | 1 |

Validations: 2014-08-30, 2014-12-09, 2014-02-02

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-08-30 | 13.96 | 13.96 | 11:40 | 11:36 | 9.55 | 9.55 | 23:45 | 23:43 |
|2014-12-09 |11.170 | 11.417 | 10:20 | 10:17 | 6.331 | 6.331 | 06:25 |06:38 |
|2014-02-02 | 7.536  | 7.536  | 14:40 | 14:38 |1.516 | 1.516 | 22:20 | 22:13 |

* On the December 9th value, it appears that the minimums observed by Portal and the minimum of the five minutes are about fifteen minutes earlier than the actual daily minimum, which was 6.295. This is within a tenth of a degree of the five minute minimum, however.

#### CENMET 450: DIFFERENCES BETWEEN FIVE-MINUTE MAX AND DAILY MAX FOR RELATIVE HUMIDITY.

* Similar to the 150 m value, the maximum difference between the two methods occurs on 2014-09-11. On this day, the daily measurement is 87.7 percent whereas the five-minute measurement is 21 percent.
* The since the values at the other height also have this discrepancy, it is acknowledged here that the 87.7 percent is more similar to the other sites (VANMET- the PRIMET 450 was not operational at this time) and to the trend of the surrounding week.
* The average percent difference in relative humidity from the mean relative humidity is 16 percent in both the five minute and daily methods.

#### PRIMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX <a id="primetmax"></a>

* ** Overview: ** 267 values collected
* ** Maximum difference ** 9.158 on 2014-11-11, after removal 0.51 on 2014-01-18

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-11-12 00:00:00 | PRIM_226_table105 | 8.24 | PRIM_226_table440 |-0.918| 

    * The five-minute maximum on this day is 8.24, although both the daily mean and the five minute mean are consistent (0.798 C five minute versus -1.21 C daily, recalling that this outlier is also certainly pulling the daily mean)
    * days preceding this one show similar daily maximums to the five-minute value of 9 C, while days following this one show similar daily maximums to the daily value, between zero and two degrees. 

* The daily maximum temperatures are on average 59 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 58 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.2 | 121 | 46 |
| 0.2 to 0.3 | 97 | 37 |
| 0.3 to 0.4 | 35 | 13 |
|0.4 to 0.5 | 11  | 0.4 |
| >0.5 | 2 | 1 |

* Besides the outlier, all values were less than half of a degree of difference between methods.

Validations: 2014-12-29, 2014-11-14, 2014-07-04

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-12-29 | 2.60 | 2.60 | 14:10 | 14:10 | -4.732 | -4.68 | 23:45 | 23:58 |
|2014-12-09 |7.19 | 7.189 | 12:45 | 12:45 | -0.345 | -0.346 | 23:55 |23:58|
|2014-07-04 | 28.19  | 28.19  | 14:15 | 14:38 |10.84 | 10.84 | 04:30 | 04:26 |

* On the 2014-12-29 and 2014-07-04 measurements, the values are similar between the Portal and METDAT, but the time of the maximum differs.

#### PRIMET 150: DIFFERENCES BETWEEN FIVE-MINUTE MAXIMUM FOR RELATIVE HUMIDITY AND THE DAILY MAXIMUM FOR RELATIVE HUMIDITY.

* The greatest difference between the five-minute and instantaneous maximums was 12 % on 2014-09-12. On this day the daily value exceeded the 5 minute value at 95 percent versus 83 percent. 
* 92 percent of differences between methods were less than 12 percent. 

#### PRIMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 266/267 values collected
* ** Maximum difference ** 8.838 on 2014-11-11, after removal of outlier, 0.68 is maximum difference which occurs on 2014-10-08.

This data on 2014-11-11 is continuously suspect, here is the 250 example. It's removal reduces the maximum difference to less than a degree

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|    
| 2014-11-12 00:00:00 |PRIM_226_table105 | 8.48 | PRIM_226_table440 |-0.358 |

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

Validations: 2014-07-30, 2014-08-22, 2014-12-07

| DATE | PORT MAX | MET MAX | PORT TMX | MET TMX| PORT MIN | MET MIN | PORT TMIN | MET TMIN|
|-|-|-|-|-|-|-|-|-|
|2014-07-30 | 33.96 | 33.96 | 13:50| 14:50 | 13.81 | 13.81 | 5:15| 5:17 |
|2014-08-22| 26.11 | 26.11| 12:45 | 12:45 | 9.18 | 9.18 | 23:55 |3:55|
|2014-12-07 | 9.33  | 9.33  | 14:40 | 14:38 |0.626 | 0.626 | 07:25 | 07:24|

#### PRIMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 266/267 values collected
* ** Maximum difference ** 8.859 on 2014-11-11, after removal it is 0.64


| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----| 
|2014-11-12 00:00:00 |PRIM_226_table105 |8.66 |PRIM_226_table440 |-0.199|

* This is the same trend as from the other sensors. 

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than 0.68 degree of difference between methods.

#### PRIMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 267 values collected
* ** Maximum difference ** 8.867 on 2014-11-11, after removal of outlier the maximum difference is only 0.45 C

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----| 
| 2014-11-12 00:00:00 | PRIM_226_table105 | 8.51 |PRIM_226_table440|-0.357|

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 55 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

#### PRIMET 450 RELATIVE HUMIDITY WAS NOT FUNCTIONING AT THIS TIME.

#### VANMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX

* ** Overview: ** 260 values collected
* ** Maximum difference ** 4.28 on 2014-06-13, once removed 0.65 on 2014-05-25

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
|2014-06-13 00:00:00|"Van_231_Table105"|"14.35"|"Van_231_Table440" |"18.63"|

* The daily maximum temperatures are on average 58.2 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 41.5 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.13 | 149 | 58 |
| 0.13 to 0.26 | 80 | 31 |
| 0.26 to 0.39 | 23 | 9 |
|0.39 to 0.52 | 6  | 2 |
| >0.52 | 2 | 1 |

* I have not yet validated these results against the results in the Portal webpage

####: VANMET 350: DIFFERENCES IN FIVE MINUTE MAX and DAILY MAX.

* on VANMET, the same september period emerges for having discrepancies between the five minute maximum and daily maximum values.
* However, the mean difference between the maximum and median relative humidty at VANMET is 20.5 degrees in the maximum values from daily and 20.4 in the version in the five minute data.
* Only 67 percent of vanmets values are within 10 percent of the mean.

#### VANMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX

* ** Overview: ** 260 values collected
* ** Maximum difference **  0.96 on 2014-06-08

* The daily maximum temperatures are on average 55.8 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 53 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.13 | 149 | 50 |
| 0.13 to 0.26 | 80 | 34 |
| 0.26 to 0.39 | 23 | 13 |
|0.39 to 0.52 | 6  | 3 |
| >0.52 | 2 | 1 |

* I have not yet validated these results against the results in the Portal webpage

#### VANMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX

* ** Overview: ** 260 values collected
* ** Maximum difference **  0.9 on 2014-06-08

* The daily maximum temperatures are on average 55.3 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 53.7 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.19 | 185 | 71 |
| 0.19 to 0.38 | 50 | 19 |
| 0.38 to 0.57 | 18 | 7 |
|0.57 to 0.76 | 5  | 2 |
| >0.76 | 2 | 1 |

* I have not yet validated these results against the results in the Portal webpage

#### VANMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX

* ** Overview: ** 258/260 values collected
* ** Maximum difference **  6.31 on 2014-06-08, once removed 0.54 on 2014-12-01

| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-06-13 00:00:00 |Van_231_Table105 | 12.94 |Van_231_Table440 |19.28|



* The daily maximum temperatures are on average 55.3 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 53.7 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

| BIN EDGES | NUMBER OF VALUES | PERCENT OF VALUES |
|--------|--------|------|
| ~0 to 0.1 | 122 | 47 |
| 0.1 to 0.2 | 78 | 30 |
| 0.2 to 0.3 | 44 | 17 |
|0.3 to 0.4 | 8  | 3 |
| >0.4 | 6 | 2 |

* I have not yet validated these results against the results in the Portal system

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

#### PRIMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.25 C on 2014- 07-21

* The daily minimum temperatures are on average 40.4 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

One outlier of note: 


| DATE | Five Minute Table | Value | Daily Table | Value |
|-----|-----|-----|-----|-----|
| 2014-06-13 00:00:00 | PRIM_226_table105 | 8.55 | PRIM_226_table440 |-23.94 |

No minimum values on PRIMET differ by more than 0.6 degrees at the 150 m height

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


#### TAKE HOME POINTS:<a id="takehome"></a>

Given the consistency between the above results, I have developed some take-home points that may be useful for future flagging.

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

#### Images: <a id="images"></a>

Here's an example of a distribution of the differences between maximum values using the daily method and using the five minute method on CENMET. It is good that there is a lot of left skew indicating that most of the differences are very small. 

<style>

</style>

<div id="fig_el7576343718117284082490231"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el7576343718117284082490231", {"axes": [{"xlim": [0.0, 0.60000000000000009], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el757634372077520"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.059979838709677422, 0.5], "rotation": -90.0, "id": "el757634372151568"}], "zoomable": true, "images": [], "xdomain": [0.0, 0.60000000000000009], "ylim": [0.0, 4.5], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el757634434670480"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el757634371983632", "ydomain": [0.0, 4.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.004000000000000448, 0.0], [0.004000000000000448, 4.384881422924892], [0.10520000000000067, 4.384881422924892], [0.10520000000000067, 3.890810276679834], [0.2064000000000009, 3.890810276679834], [0.2064000000000009, 1.2351778656126458], [0.3076000000000011, 1.2351778656126458], [0.3076000000000011, 0.3087944664031613], [0.40880000000000133, 0.3087944664031613], [0.40880000000000133, 0.06175889328063226], [0.5100000000000016, 0.06175889328063226], [0.5100000000000016, 0.0], [0.40880000000000133, 0.0], [0.40880000000000133, 0.0], [0.3076000000000011, 0.0], [0.3076000000000011, 0.0], [0.2064000000000009, 0.0], [0.2064000000000009, 0.0], [0.10520000000000067, 0.0], [0.10520000000000067, 0.0]]}, "id": "el757634371811728"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el7576343718117284082490231", {"axes": [{"xlim": [0.0, 0.60000000000000009], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el757634372077520"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.059979838709677422, 0.5], "rotation": -90.0, "id": "el757634372151568"}], "zoomable": true, "images": [], "xdomain": [0.0, 0.60000000000000009], "ylim": [0.0, 4.5], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el757634434670480"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el757634371983632", "ydomain": [0.0, 4.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.004000000000000448, 0.0], [0.004000000000000448, 4.384881422924892], [0.10520000000000067, 4.384881422924892], [0.10520000000000067, 3.890810276679834], [0.2064000000000009, 3.890810276679834], [0.2064000000000009, 1.2351778656126458], [0.3076000000000011, 1.2351778656126458], [0.3076000000000011, 0.3087944664031613], [0.40880000000000133, 0.3087944664031613], [0.40880000000000133, 0.06175889328063226], [0.5100000000000016, 0.06175889328063226], [0.5100000000000016, 0.0], [0.40880000000000133, 0.0], [0.40880000000000133, 0.0], [0.3076000000000011, 0.0], [0.3076000000000011, 0.0], [0.2064000000000009, 0.0], [0.2064000000000009, 0.0], [0.10520000000000067, 0.0], [0.10520000000000067, 0.0]]}, "id": "el757634371811728"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el7576343718117284082490231", {"axes": [{"xlim": [0.0, 0.60000000000000009], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el757634372077520"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.059979838709677422, 0.5], "rotation": -90.0, "id": "el757634372151568"}], "zoomable": true, "images": [], "xdomain": [0.0, 0.60000000000000009], "ylim": [0.0, 4.5], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el757634434670480"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el757634371983632", "ydomain": [0.0, 4.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.004000000000000448, 0.0], [0.004000000000000448, 4.384881422924892], [0.10520000000000067, 4.384881422924892], [0.10520000000000067, 3.890810276679834], [0.2064000000000009, 3.890810276679834], [0.2064000000000009, 1.2351778656126458], [0.3076000000000011, 1.2351778656126458], [0.3076000000000011, 0.3087944664031613], [0.40880000000000133, 0.3087944664031613], [0.40880000000000133, 0.06175889328063226], [0.5100000000000016, 0.06175889328063226], [0.5100000000000016, 0.0], [0.40880000000000133, 0.0], [0.40880000000000133, 0.0], [0.3076000000000011, 0.0], [0.3076000000000011, 0.0], [0.2064000000000009, 0.0], [0.2064000000000009, 0.0], [0.10520000000000067, 0.0], [0.10520000000000067, 0.0]]}, "id": "el757634371811728"});
            })
         });
}
</script>

Here's a sample distribution on PRIMET, 150 m. 


<style>

</style>

<div id="fig_el8906543718156961093860287"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el8906543718156961093860287", {"axes": [{"xlim": [0.0, 14.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el890654372093968"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076612903225806453, 0.5], "rotation": -90.0, "id": "el890654372159056"}], "zoomable": true, "images": [], "xdomain": [0.0, 14.0], "ylim": [0.0, 0.40000000000000002], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el890654434669264"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el890654371971408", "ydomain": [0.0, 0.40000000000000002], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.3793018379178489], [2.419999999999999, 0.3793018379178489], [2.419999999999999, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [7.259999999999997, 0.015418773899099548], [7.259999999999997, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099555], [12.099999999999994, 0.0015418773899099555], [12.099999999999994, 0.0], [9.679999999999996, 0.0], [9.679999999999996, 0.0], [7.259999999999997, 0.0], [7.259999999999997, 0.0], [4.839999999999998, 0.0], [4.839999999999998, 0.0], [2.419999999999999, 0.0], [2.419999999999999, 0.0]]}, "id": "el890654371815696"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el8906543718156961093860287", {"axes": [{"xlim": [0.0, 14.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el890654372093968"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076612903225806453, 0.5], "rotation": -90.0, "id": "el890654372159056"}], "zoomable": true, "images": [], "xdomain": [0.0, 14.0], "ylim": [0.0, 0.40000000000000002], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el890654434669264"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el890654371971408", "ydomain": [0.0, 0.40000000000000002], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.3793018379178489], [2.419999999999999, 0.3793018379178489], [2.419999999999999, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [7.259999999999997, 0.015418773899099548], [7.259999999999997, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099555], [12.099999999999994, 0.0015418773899099555], [12.099999999999994, 0.0], [9.679999999999996, 0.0], [9.679999999999996, 0.0], [7.259999999999997, 0.0], [7.259999999999997, 0.0], [4.839999999999998, 0.0], [4.839999999999998, 0.0], [2.419999999999999, 0.0], [2.419999999999999, 0.0]]}, "id": "el890654371815696"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el8906543718156961093860287", {"axes": [{"xlim": [0.0, 14.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el890654372093968"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076612903225806453, 0.5], "rotation": -90.0, "id": "el890654372159056"}], "zoomable": true, "images": [], "xdomain": [0.0, 14.0], "ylim": [0.0, 0.40000000000000002], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el890654434669264"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el890654371971408", "ydomain": [0.0, 0.40000000000000002], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.3793018379178489], [2.419999999999999, 0.3793018379178489], [2.419999999999999, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [4.839999999999998, 0.015418773899099548], [7.259999999999997, 0.015418773899099548], [7.259999999999997, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099551], [9.679999999999996, 0.0015418773899099555], [12.099999999999994, 0.0015418773899099555], [12.099999999999994, 0.0], [9.679999999999996, 0.0], [9.679999999999996, 0.0], [7.259999999999997, 0.0], [7.259999999999997, 0.0], [4.839999999999998, 0.0], [4.839999999999998, 0.0], [2.419999999999999, 0.0], [2.419999999999999, 0.0]]}, "id": "el890654371815696"});
            })
         });
}
</script>

Here are some images from Relative Humidity, doing the same analyses

 Differences in Maximums on CENMET for Relative Humidity


<style>

</style>

<div id="fig_el894314439172816866256538"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el894314439172816866256538", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438995536"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314438727952"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.089999999999999997], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314371179792"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439448720", "ydomain": [0.0, 0.089999999999999997], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.082785298174716], [11.026, 0.082785298174716], [11.026, 0.0036910642498281018], [22.052, 0.0036910642498281018], [22.052, 0.002636474464162929], [33.078, 0.002636474464162929], [33.078, 0.0010545897856651723], [44.104, 0.0010545897856651723], [44.104, 0.0005272948928325862], [55.129999999999995, 0.0005272948928325862], [55.129999999999995, 0.0], [44.104, 0.0], [44.104, 0.0], [33.078, 0.0], [33.078, 0.0], [22.052, 0.0], [22.052, 0.0], [11.026, 0.0], [11.026, 0.0]]}, "id": "el894314439172816"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el894314439172816866256538", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438995536"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314438727952"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.089999999999999997], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314371179792"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439448720", "ydomain": [0.0, 0.089999999999999997], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.082785298174716], [11.026, 0.082785298174716], [11.026, 0.0036910642498281018], [22.052, 0.0036910642498281018], [22.052, 0.002636474464162929], [33.078, 0.002636474464162929], [33.078, 0.0010545897856651723], [44.104, 0.0010545897856651723], [44.104, 0.0005272948928325862], [55.129999999999995, 0.0005272948928325862], [55.129999999999995, 0.0], [44.104, 0.0], [44.104, 0.0], [33.078, 0.0], [33.078, 0.0], [22.052, 0.0], [22.052, 0.0], [11.026, 0.0], [11.026, 0.0]]}, "id": "el894314439172816"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el894314439172816866256538", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438995536"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314438727952"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.089999999999999997], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314371179792"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439448720", "ydomain": [0.0, 0.089999999999999997], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.082785298174716], [11.026, 0.082785298174716], [11.026, 0.0036910642498281018], [22.052, 0.0036910642498281018], [22.052, 0.002636474464162929], [33.078, 0.002636474464162929], [33.078, 0.0010545897856651723], [44.104, 0.0010545897856651723], [44.104, 0.0005272948928325862], [55.129999999999995, 0.0005272948928325862], [55.129999999999995, 0.0], [44.104, 0.0], [44.104, 0.0], [33.078, 0.0], [33.078, 0.0], [22.052, 0.0], [22.052, 0.0], [11.026, 0.0], [11.026, 0.0]]}, "id": "el894314439172816"});
            })
         });
}
</script>


Differences between "Minimums" in Relative Humidity on CENMET, 150

<style>

</style>

<div id="fig_el894314436265552162221783"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el894314436265552162221783", {"axes": [{"xlim": [0.0, 70.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314439282576"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314440887120"}], "zoomable": true, "images": [], "xdomain": [0.0, 70.0], "ylim": [0.0, 0.040000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438770000"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436364368", "ydomain": [0.0, 0.040000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.09000000000000341, 0.0], [0.09000000000000341, 0.03865780114427091], [13.024000000000004, 0.03865780114427091], [13.024000000000004, 0.024273503044077084], [25.958000000000006, 0.024273503044077084], [25.958000000000006, 0.008540676996990083], [38.89200000000001, 0.008540676996990083], [38.89200000000001, 0.004045583840679515], [51.82600000000001, 0.004045583840679515], [51.82600000000001, 0.0017980372625242289], [64.76, 0.0017980372625242289], [64.76, 0.0], [51.82600000000001, 0.0], [51.82600000000001, 0.0], [38.89200000000001, 0.0], [38.89200000000001, 0.0], [25.958000000000006, 0.0], [25.958000000000006, 0.0], [13.024000000000004, 0.0], [13.024000000000004, 0.0]]}, "id": "el894314436265552"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el894314436265552162221783", {"axes": [{"xlim": [0.0, 70.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314439282576"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314440887120"}], "zoomable": true, "images": [], "xdomain": [0.0, 70.0], "ylim": [0.0, 0.040000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438770000"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436364368", "ydomain": [0.0, 0.040000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.09000000000000341, 0.0], [0.09000000000000341, 0.03865780114427091], [13.024000000000004, 0.03865780114427091], [13.024000000000004, 0.024273503044077084], [25.958000000000006, 0.024273503044077084], [25.958000000000006, 0.008540676996990083], [38.89200000000001, 0.008540676996990083], [38.89200000000001, 0.004045583840679515], [51.82600000000001, 0.004045583840679515], [51.82600000000001, 0.0017980372625242289], [64.76, 0.0017980372625242289], [64.76, 0.0], [51.82600000000001, 0.0], [51.82600000000001, 0.0], [38.89200000000001, 0.0], [38.89200000000001, 0.0], [25.958000000000006, 0.0], [25.958000000000006, 0.0], [13.024000000000004, 0.0], [13.024000000000004, 0.0]]}, "id": "el894314436265552"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el894314436265552162221783", {"axes": [{"xlim": [0.0, 70.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314439282576"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314440887120"}], "zoomable": true, "images": [], "xdomain": [0.0, 70.0], "ylim": [0.0, 0.040000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438770000"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 8, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 10, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436364368", "ydomain": [0.0, 0.040000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.09000000000000341, 0.0], [0.09000000000000341, 0.03865780114427091], [13.024000000000004, 0.03865780114427091], [13.024000000000004, 0.024273503044077084], [25.958000000000006, 0.024273503044077084], [25.958000000000006, 0.008540676996990083], [38.89200000000001, 0.008540676996990083], [38.89200000000001, 0.004045583840679515], [51.82600000000001, 0.004045583840679515], [51.82600000000001, 0.0017980372625242289], [64.76, 0.0017980372625242289], [64.76, 0.0], [51.82600000000001, 0.0], [51.82600000000001, 0.0], [38.89200000000001, 0.0], [38.89200000000001, 0.0], [25.958000000000006, 0.0], [25.958000000000006, 0.0], [13.024000000000004, 0.0], [13.024000000000004, 0.0]]}, "id": "el894314436265552"});
            })
         });
}
</script>

Differences in Maximums on Vanmet for Relative Humidity

<style>

</style>

<div id="fig_el8943144392849445631979735"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el8943144392849445631979735", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314371109392"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314436413584"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.070000000000000007], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314441008400"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 9, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439253776", "ydomain": [0.0, 0.070000000000000007], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.06223297608048893], [10.774000000000001, 0.06223297608048893], [10.774000000000001, 0.016358382284014233], [21.548000000000002, 0.016358382284014233], [21.548000000000002, 0.005689872098787559], [32.322, 0.005689872098787559], [32.322, 0.005334255092613337], [43.096000000000004, 0.005334255092613337], [43.096000000000004, 0.0032005530555680017], [53.870000000000005, 0.0032005530555680017], [53.870000000000005, 0.0], [43.096000000000004, 0.0], [43.096000000000004, 0.0], [32.322, 0.0], [32.322, 0.0], [21.548000000000002, 0.0], [21.548000000000002, 0.0], [10.774000000000001, 0.0], [10.774000000000001, 0.0]]}, "id": "el894314439284944"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el8943144392849445631979735", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314371109392"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314436413584"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.070000000000000007], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314441008400"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 9, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439253776", "ydomain": [0.0, 0.070000000000000007], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.06223297608048893], [10.774000000000001, 0.06223297608048893], [10.774000000000001, 0.016358382284014233], [21.548000000000002, 0.016358382284014233], [21.548000000000002, 0.005689872098787559], [32.322, 0.005689872098787559], [32.322, 0.005334255092613337], [43.096000000000004, 0.005334255092613337], [43.096000000000004, 0.0032005530555680017], [53.870000000000005, 0.0032005530555680017], [53.870000000000005, 0.0], [43.096000000000004, 0.0], [43.096000000000004, 0.0], [32.322, 0.0], [32.322, 0.0], [21.548000000000002, 0.0], [21.548000000000002, 0.0], [10.774000000000001, 0.0], [10.774000000000001, 0.0]]}, "id": "el894314439284944"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el8943144392849445631979735", {"axes": [{"xlim": [0.0, 60.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314371109392"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.076675907258064516, 0.5], "rotation": -90.0, "id": "el894314436413584"}], "zoomable": true, "images": [], "xdomain": [0.0, 60.0], "ylim": [0.0, 0.070000000000000007], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314441008400"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 9, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314439253776", "ydomain": [0.0, 0.070000000000000007], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.06223297608048893], [10.774000000000001, 0.06223297608048893], [10.774000000000001, 0.016358382284014233], [21.548000000000002, 0.016358382284014233], [21.548000000000002, 0.005689872098787559], [32.322, 0.005689872098787559], [32.322, 0.005334255092613337], [43.096000000000004, 0.005334255092613337], [43.096000000000004, 0.0032005530555680017], [53.870000000000005, 0.0032005530555680017], [53.870000000000005, 0.0], [43.096000000000004, 0.0], [43.096000000000004, 0.0], [32.322, 0.0], [32.322, 0.0], [21.548000000000002, 0.0], [21.548000000000002, 0.0], [10.774000000000001, 0.0], [10.774000000000001, 0.0]]}, "id": "el894314439284944"});
            })
         });
}
</script>

Differences in Minimums on VANMET for relative humidity.

<style>

</style>

<div id="fig_el8943144362665127506890787"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){
       
       mpld3.draw_figure("fig_el8943144362665127506890787", {"axes": [{"xlim": [0.0, 90.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438481936"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314439448208"}], "zoomable": true, "images": [], "xdomain": [0.0, 90.0], "ylim": [0.0, 0.025000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438854160"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 10, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436572944", "ydomain": [0.0, 0.025000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.024661998502664376], [17.4, 0.024661998502664376], [17.4, 0.01629453472497468], [34.8, 0.01629453472497468], [34.8, 0.008807856608094421], [52.199999999999996, 0.008807856608094421], [52.199999999999996, 0.006165499625666094], [69.6, 0.006165499625666094], [69.6, 0.0015413749064165229], [87.0, 0.0015413749064165229], [87.0, 0.0], [69.6, 0.0], [69.6, 0.0], [52.199999999999996, 0.0], [52.199999999999996, 0.0], [34.8, 0.0], [34.8, 0.0], [17.4, 0.0], [17.4, 0.0]]}, "id": "el894314436266512"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
         
         mpld3.draw_figure("fig_el8943144362665127506890787", {"axes": [{"xlim": [0.0, 90.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438481936"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314439448208"}], "zoomable": true, "images": [], "xdomain": [0.0, 90.0], "ylim": [0.0, 0.025000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438854160"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 10, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436572944", "ydomain": [0.0, 0.025000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.024661998502664376], [17.4, 0.024661998502664376], [17.4, 0.01629453472497468], [34.8, 0.01629453472497468], [34.8, 0.008807856608094421], [52.199999999999996, 0.008807856608094421], [52.199999999999996, 0.006165499625666094], [69.6, 0.006165499625666094], [69.6, 0.0015413749064165229], [87.0, 0.0015413749064165229], [87.0, 0.0], [69.6, 0.0], [69.6, 0.0], [52.199999999999996, 0.0], [52.199999999999996, 0.0], [34.8, 0.0], [34.8, 0.0], [17.4, 0.0], [17.4, 0.0]]}, "id": "el894314436266512"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){
                 
                 mpld3.draw_figure("fig_el8943144362665127506890787", {"axes": [{"xlim": [0.0, 90.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [{"v_baseline": "hanging", "h_anchor": "middle", "color": "#000000", "text": "Value", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [0.5, -0.059895833333333329], "rotation": -0.0, "id": "el894314438481936"}, {"v_baseline": "auto", "h_anchor": "middle", "color": "#000000", "text": "Probability", "coordinates": "axes", "zorder": 3, "alpha": 1, "fontsize": 12.0, "position": [-0.09375, 0.5], "rotation": -90.0, "id": "el894314439448208"}], "zoomable": true, "images": [], "xdomain": [0.0, 90.0], "ylim": [0.0, 0.025000000000000001], "paths": [{"edgecolor": "#000000", "facecolor": "#FF0000", "edgewidth": 1.0, "pathcodes": ["M", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "Z"], "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 1, "alpha": 1, "xindex": 0, "data": "data01", "id": "el894314438854160"}], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "bottom", "nticks": 10, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 12.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [], "markers": [], "id": "el894314436572944", "ydomain": [0.0, 0.025000000000000001], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[0.0, 0.0], [0.0, 0.024661998502664376], [17.4, 0.024661998502664376], [17.4, 0.01629453472497468], [34.8, 0.01629453472497468], [34.8, 0.008807856608094421], [52.199999999999996, 0.008807856608094421], [52.199999999999996, 0.006165499625666094], [69.6, 0.006165499625666094], [69.6, 0.0015413749064165229], [87.0, 0.0015413749064165229], [87.0, 0.0], [69.6, 0.0], [69.6, 0.0], [52.199999999999996, 0.0], [52.199999999999996, 0.0], [34.8, 0.0], [34.8, 0.0], [17.4, 0.0], [17.4, 0.0]]}, "id": "el894314436266512"});
            })
         });
}
</script>