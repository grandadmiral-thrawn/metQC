---
layout: post
title: "Can Daily Minimums and Maximums Be Found From Five Minute Means?"
date: 2015-03-24T18:19:40-07:00
---

We tested if the daily maximum and minimum values that were calculated by the logger in the daily instruction could be reasonably replaced by five minuate calculations since in the future we will be using the five-minute calculations exclusively. We wanted to find out if the maximums and minimums of the (hopefully!) 288 five-minute mean values over the day would be similar to the maximum or minimum which would have been instantaneously calculated by the logger. We wanted to test this on air-temperature, relative-humidity, dew-point, and solar. The jargon can be confusing so:

* I will call the daily measurements as computed by the logger "instantaneous" e.g. "instantaneous maximum of air temperature is 24 C, at 14:03"

* I will call the maximum of the five-minute measurements "five-minute" e.g. "five-minute maximum of air temperature is 23.9 C, at 14:05". The same convention will apply for "fifteen-minute" and "hourly" maximums

The original analysis is [here](http://dataronin.github.io/metQC/2015/02/10/min_max_checks.html). Here is a brief overview of what we found:

#### AIR TEMPERATURE MAXIMUMS

Instantaneous maximums from all sites were within less than one degree of difference from five-minute maximums. The time interval could vary by up to ten minutes if the maximum occured during a very hot part of the day. Air temperature maximums both instantaneous and five-minute were approximately 60 percent greater than the daily mean. We also compared the fifteen-minute maximums to the instantaneous maximums, and at this scale there was often more than a degree of difference.

##### A bar chart of the difference between the instantaneous maximum for the day and the maximum five minute mean on CENMET at 150 height:


<style>

.chart div {
  font: 10px sans-serif;
  background-color: blue;
  text-align: right;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-right: 3px;
  padding-left: 3px;
  margin: 10px;
  color: white;
}

</style>
<div class="chart">
  <div style="width: 440px;">Less Than 0.1 C</div>
  <div style="width: 390px;">0.1 C to O.2 C</div>
  <div style="width: 130px;">0.2 C to 0.3 C</div>
  <div style="width: 30px;">0.3 C +</div>
</div>

* RELATIVE HUMIDITY MAXIMUMS: Relative humidity maximum is constrained at 100 percent, so comparisons were less robust. However, most of our high-resolution data for relative humidity is at an hourly basis. On an hourly basis, there was a mean difference of twelve-percent between hourly maximums and instantaneous maximums. Since relative humidity often reaches 100 percent, the average standard deviation of relative humidity maximums over one day was twenty percent. We would not be concerned even now with using the maximum daily relative humidity value on days where the relative humidity reaches 100 percent. If we were to calculate relative humidity at a five-minute resolution, this would likely reduce the difference between daily and hourly maximums.

* DEW POINT MAXIMUMS and VPD MAXIMUMS: These are largely subject to the quality of air temperature and relative humidity maximums. With five-minute temperatures and relative humidities, dew points and vapor pressure deficits are generally very similar in five-minute maximums to daily maximums. However, the issue of data quality greatly hinders these analyses.  Sometimes dew point is "calculated" even when both relative humidity and air temperature are off (see the [flags](http://dataronin.github.io/metQC/2015/02/09/outline_of_flags_and_problems_on_portal.html) document). When erroneous dew-point calculations were removed, the majority of dew points maximums were less than two degrees different than the five minute maximums. The key to a calculated dew point maximum will be very quality controlled five-minute data.

* AIR TEMPERATURE MINIMUMS: These are also within less than one degree of difference from the five minute minimums. The minimums with both methods were about 40 percent less than the daily mean. In general, there was less variability between minimums than maximums. Recently, on PRIMET at 450 m there were several outlier measurements. WE ALSO HAPPEN TO BE MISSING ALL OF THE OTHER MEASUREMENTS NEEDED HERE ON PRIMET 450!

* RELATIVE HUMIDITY MINIMUMS: The instantaneous relative humidity minimums can be very different than the five minute minimums. The average daily range of the relative humidity minimum as calculated from five-minute and hourly data is 40 percent. Consequently, there are also days where the minimum does not change at all, nor drop below 100 percent. 

* DEW POINT MINIMUMS: The average difference between dew point minimum between the instantaneous and five-minute method was about 1.5 degrees C.  When using the five minute method, the minimum dew point was usually about 29 percent lower than the daily mean dew point; when using the instantaneous method it was about 33 percent lower. The most nefarious problem with dew points is the calculation of the dew point in the log even when relative humidity or air temperature are missing. 