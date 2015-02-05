---
layout: post
title: "Min_max_checks"
date: 2015-02-03T14:30:24-08:00
---

# Table of Contents
  * [The Problem](#qlink)
  * [The Approach](#approach)
  * [Basic Statistics for Air Temperature](#statlink)


## The Problem<a id="qlink"></a>

Data collected on METDAT of the instantaneous minimum and maximum temperature occuring on a single day is no longer being maintained. Recently, we have used the best five- or fifteen- minute maximum from the day to approximate these instantaneous values. But are they really the same?

Example (hypothetical):

* Instantaneous maximum is "37.89" and occurs at 12:34:05
* Five- minute preceding temperature is "36.35" at 12:30:00 and following is "35.87" at 12:35:00. 
* ** Question ** How important is it to capture the instantaneous values?

## The Approach<a id="approach"></a>

## Basic Statistics for Air Temperature<a id= "statlink"></a>

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

The table here describes the histogram results. I divided each data set into 5 evenly spaced bins. In the case where the number of values is less than the total shared days, the individual attribute may have some NULL values which cannot be compared.

#### CENMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

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

#### PRIMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 267 values collected
* ** Maximum difference ** 9.158 on 2014-11-11
    
    * The five-minute maximum on this day is 8.24, although both the daily mean and the five minute mean are consistent (0.798 C fiveminute versus -1.21 C daily, recalling that this outlier is also certainly pulling the daily mean)
    * days preceding this one show similar daily maximums to the five-minute value of 9 C, while days following this one show similar daily maximums to the daily value, between zero and two degrees. 

* The daily maximum temperatures are on average 59 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 58 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

#### PRIMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 267 values collected
* ** Maximum difference ** 8.838 on 2014-11-11
    
    * Same trend regarding daily maximums as in the 150 sensor 

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

#### PRIMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 267 values collected
* ** Maximum difference ** 8.859 on 2014-11-11
    
    * Same trend regarding daily maximums as in the 150 and 250 sensr 

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

#### PRIMET 450 : DIFFERENCES BETWEEN FIVE-MINUTE MAX and DAILY MAX 

* ** Overview: ** 267 values collected
* ** Maximum difference ** 8.867 on 2014-11-11
    
    * Same trend regarding daily maximums as in the 150,250, and 350 sensor 

* The daily maximum temperatures are on average 56 percent greater than the mean temperature for the day as calculated on the daily summary
* The five-minute maximum temperatures are on average 55 percent greater than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

* Besides the outlier, all values were less than one degree of difference between methods.

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

#### PRIMET 150 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.25 C on 2014- 07-21

* The daily minimum temperatures are on average 40.4 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

One outlier of note: 

"2014-06-13 00:00:00","PRIM_226_table105","12.6153","19.98","8.55","PRIM_226_table440","12.61","20.14","-23.94","2014-06-12 08:25:16.500000","2014-06-12 08:25:16.500000",0.16000000000000014,32.49,0.5838,0.5971,0.3223,2.8985

No minimum values on PRIMET differ by more than 0.6 degrees at the 150 m height

#### PRIMET 250 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.21 C on 2014-07-21

* The daily minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.4 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 


No minimum values on PRIMET differ by more than 0.6 degrees at the 250 m height

#### PRIMET 350 : DIFFERENCES BETWEEN FIVE-MINUTE MIN and DAILY MIN 

* ** Overview: ** 267 / 267 values collected
* ** Maximum difference ** 0.19 C on 2014-07-21

* The daily minimum temperatures are on average 39.5 percent less than the mean temperature for the day as calculated on the daily summary
* The five-minute minimum temperatures are on average 39.4 percent less than the mean temperature for the day as calculated as the mean of all the five minute temperatures
* ** Note: ** the above "averages" are actually medians to remove outlier effect 

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



"2014-07-04 00:00:00","Van_231_Table105","13.6798","21.45","6.542","Van_231_Table440","13.67","26.29","-43.38","2014-07-03 11:43:45","2014-07-03 11:42:00",4.84,49.922000000000004,0.568,0.9232,0.5218,4.1734

#### TAKE HOME POINTS:

* maximums are about 65 percent greater than daily mean in both five minute and instantaneous methods
* differences in maximums increases VERY SLIGHTLY with height on sensor
* minumums are about 40 percent less than daily mean in both five minute and instantaneous methods
* minimums do not seem to change much with sensor height
* all of the max daily temperatures from instantaneous are less than one and a half degrees off the five- minute values
* this analysis treated days as "calendar days". 


* ** Data Quality may be questionable in some cases, ex.:** Reports in METDAT (table CENT_233_Table440) are slightly different (rounding?) than those on Portal:

    * 19.88, Jan. 26 2015 01:50:15:000PM
    * 20.22, Jan. 26 2015 01:43:30:000PM
    * 20.49, Jan. 26 2015 01:43:30:000PM
    * 20.27, Jan. 26 2015 01:43:30:000PM

* Portal Reports for cenmet_233_a_dly_2015.csv (these are the daily values):
 
    * at height 150: 19.700,"",13:55:00
    * at height 250, 20.070,"",13:50:00
    * at height 350, 20.360,"",13:45:00
    * at height 450, 20.140,"",13:45:00


#### Images: 



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