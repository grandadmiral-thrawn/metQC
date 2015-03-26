---
layout: post
title: "Can Daily Minimums and Maximums Be Found From Five Minute Means?"
date: 2015-03-24T18:19:40-07:00
---

We tested if the daily maximum and minimum values that were calculated by the logger in the daily instruction could be reasonably replaced by five minuate calculations since in the future we will be using the five-minute calculations exclusively. We wanted to find out if the maximums and minimums of the (hopefully!) 288 five-minute mean values over the day would be similar to the maximum or minimum which would have been instantaneously calculated by the logger.

We wanted to test this on air-temperature, relative-humidity, dew-point, and solar. On this page I will just address the temperature, relative humidity, and dew point, with the understanding that vapor pressure defecit, like dew point, depends on relative humidity and temperature. This analysis is confusing to describe so:

* I will call the daily measurements as computed by the logger "instantaneous" e.g. "instantaneous maximum of air temperature is 24 C, at 14:03"

* I will call the maximum of the five-minute measurements "five-minute" e.g. "five-minute maximum of air temperature is 23.9 C, at 14:05". The same convention will apply for "fifteen-minute" and "hourly" maximums

The original analysis is [here](http://dataronin.github.io/metQC/2015/02/10/min_max_checks.html). 

In my view, the most important outcome(s) are 

1. The five minute results are good surrogates for temperature and relative humidity daily values...IF...

2. Flags are propogated in the right order from the air temperature to the dew point and from the relative humidity to the dew point. If bad dew points are not flagged, they are often in the range where they will get chosen as a daily extreme value. So, implementing our daily flagging algorithm in the GCE is absolutely top priority.

Here is a brief overview of what we found:

#### AIR TEMPERATURE MAXIMUMS AND MINIMUMS

Instantaneous maximums and minimums from all sites were within less than one degree of difference from five-minute maximums. The time interval could vary by up to ten minutes if the maximum occured during a very hot part of the day. Air temperature maximums both instantaneous and five-minute were approximately 60 percent greater than the daily mean. We also compared the fifteen-minute maximums to the instantaneous maximums, and at this scale there was often more than a degree of difference. There were also a larger number of outliers on PRIMET than on other stations.

##### A bar chart of the difference between the instantaneous maximum for the day and the maximum five minute mean on CENMET at 150 height. More than 85 % of values have less than 0.2 C difference between the daily instantaneous maximum and the maximum of five minute means.


<style>

.chart div {
  font: 10px sans-serif;
  background-color: #990033;
  text-align: right;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-right: 3px;
  padding-left: 3px;
  margin-left: 100px;
  margin-bottom: 1px;
  margin-top: 1px;

  color: white;
}

</style>
<div class="chart">
  <div style="width: 440px;">Less Than 0.1 C</div>
  <div style="width: 390px;">0.1 C to O.2 C</div>
  <div style="width: 130px;">0.2 C to 0.3 C</div>
  <div style="width: 30px;">0.3 C+</div>
</div>



#### RELATIVE HUMIDITY MAXIMUMS 

Relative humidity maximum is constrained at 100 percent, so comparisons were less robust. However, most of our high-resolution data for relative humidity is at an hourly basis. On an hourly basis, there was a mean difference of twelve percent between hourly maximums and instantaneous maximums. On the two loggers we have at 5-minute resolution, VANMET and CENMET, about 85 percent of relative humidities were less than 10 percent different between the instantaneous maximum and the five minute maximum.  

##### A bar chart of the difference between the instantaneous maximum for the day and the maximum five minute mean on CENMET at 450 height. 82 % of values have less than 10 percent difference between the daily instantaneous maximum and the maximum of five minute means. On VANMET at the same height there is 88% of values that are less than 10% different.


<style>

.bchart div {
  font: 10px sans-serif;
  background-color: #6600CC;
  text-align: right;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-right: 3px;
  padding-left: 3px;
  margin-left: 100px;
  margin-bottom: 1px;
  margin-top: 1px;

  color: white;
}
</style>
##### CENMET 450m RELATIVE HUMIDITY 

<div class="bchart">
  <div style="width: 410px;">Less than 10 %</div>
  <div style="width: 50px;"> 10-20 %</div>
  <div style="width: 40px;"> 20+ %</div>
</div>
##### VANMET 450m RELATIVE HUMIDITY

<div class="chart">
  <div style="width: 435px;">Less than 10 %</div>
  <div style="width: 50px;"> 10-20 %</div>
  <div style="width: 25px;"> 20+ %</div>
</div>

Since relative humidity often reaches 100 percent, the average standard deviation of relative humidity maximums over one day was twenty percent. We would not be concerned even now with using the maximum daily relative humidity value on days where the relative humidity reaches 100 percent. If we were to calculate relative humidity at a five-minute resolution, this would likely reduce the difference between daily and hourly maximums.


#### RELATIVE HUMIDITY MINIMUMS

The instantaneous relative humidity minimums can be very different than the five minute minimums. The average daily range of the relative humidity minimum as calculated from five-minute and hourly data is 40 percent. On VANMET in particular I noticed that even when the 5 minute relative humidity was 100 percent all day, the instantaneous  relative humidity could be much lower. 

#### DEW POINT MAXIMUMS AND MINIMUMS

These are largely subject to the quality of air temperature and relative humidity maximums. With five-minute temperatures and relative humidities, dew points and vapor pressure deficits are generally very similar in five-minute maximums to daily maximums. However, the issue of data quality greatly hinders these analyses.  Sometimes dew point is "calculated" even when both relative humidity and air temperature are off (see the [flags](http://dataronin.github.io/metQC/2015/02/09/outline_of_flags_and_problems_on_portal.html) document). This is a real problem. When erroneous dew-point calculations were removed, the majority of dew points maximums were less than two degrees different than the five minute maximums. The key to a calculated dew point maximum will be very quality controlled five-minute data.
<style>

.cchart div {
  font: 10px sans-serif;
  background-color: #6699FF;
  text-align: right;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-right: 3px;
  padding-left: 3px;
  margin-left: 100px;
  margin-bottom: 1px;
  margin-top: 1px;

  color: white;
}
</style>

##### Dew points on CENMET at 150 m height were very similar between the maxmimum for the day and the five minute maximums.

<div class="cchart">
  <div style="width: 435px;">Less Than 0.1 C</div>
  <div style="width: 45px;">0.1 C to O.2 C</div>
  <div style="width: 25px;">0.2 C +</div>
</div>

Similar to dew point maximums, the dew point minimums at five minutes really suffer from quality problems. Because the dew point can be calculated when the relative humidity and air temperature are not present (an error) and because these calculations, for whatever reason, tend to be on the order of "-70 C", the dew point minimum often gets chosen incorrectly when picking amongst five minute means. Once again, proactive flagging is critical to managing dew points on a five-minute scale. 
 