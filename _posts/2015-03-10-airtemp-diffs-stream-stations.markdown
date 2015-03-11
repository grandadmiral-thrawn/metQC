---
layout: post
title: "Air Temperature Differences Between Gaged Stream Stations"
date: 2015-03-10T14:28:38-07:00
---

Air Temperatures are also measured at the gaged stream stations, but unlike water temperatures, they are on a 15 minute scale. As expected, the air temperatures are more variable than the water temperatures. See the stream temperature [post](http://dataronin.github.io/metQC/2015/03/10/stream-temperature-difference-calibrations.html)  for more details on this structure. 

Essentially, the first information given is basic statistics about the temperature, the duplicates section is a QC section for METDAT database, listing when times are duplicated but values are different, and the questionable values, in this case, are changes > 10 C that occur over time interval (either 15 minutes or an hour).

It had been noted that WS10 air temperature seems to have a lot of fluctuations as compared to the other stations. While this is true, all the stations did show more variability than I would have expected off hand.

Flagging thoughts:
----------------

#### * at 15 minutes air temperature difference flags should be 1.25 C
#### * at an hour, they should be 5 C. 

This will get 4 sigma for all sites (except lower McRae, which is 5.2).


WS01 
-----

* mean hourly change: 0.627
* hourly std: 0.667
* hourly  four std + : 3.297
* hourly  three std +: 2.63
* hourly  median : 0.4 
* hourly  max: 6.7

* 15-min change: 0.178
* 15-min std: 0.194
* 15-min four std + : 0.952
* 15-min three std +: 0.758 
* 15-min median : 0.120
* 15-min max: 5.620

Duplicates with different values  
-------------

| date | value of air T |
| - | - |
| 2012-05-23 00:00 | 6.506 |
| 2013-10-23 00:15 | 7.099 |


example:

        2013-10-23 00:15:00.0000000 52269   101 5655    2013    296 15  7.19    9.45    9.34
        2013-10-23 00:15:00.0000000 52270   101 5655    2013    296 15  7.1 9.440001    9.32



WS02 
-----

* mean hourly change: 0.532
* hourly std: 0.545
* hourly four std + : 2.711
* hourly three std +: 2.166
* hourly median : 0.4 
* hourly max: 8.9

* mean 15-min change: 0.156 
* 15-min std: 0.158
* 15-min four std + : 0.789
* 15-min three std +: 0.631
* 15-min median : 0.110
* 15-min max: 2.81


Duplicates with different values 
-------------

| date | value of air T |
| - | - |
| 2012-05-08 17:00 | 16.060 |
| 2012-05-08 17:15 | 15.840|
| 2012-05-08 17:30 | 15.590 |
| 2012-05-08 17:45 | 15.410 |
| 2012-05-22 00:00 | 9.210 |


WS03 
------

* mean hourly change: 0.646 
* hourly std: 0.693
* hourly four std + : 3.419
* hourly three std +: 2.725 
* hourly median : 0.4 
* hourly max: 6.5

* 15-min change: 0.172
* 15-min std: 0.198
* 15-min four std + : 0.963
* 15-min three std +: 0.765
* 15-min median : 0.117
* 15-min max: 5.102


Duplicates with different values
-------------

| date | value of air T |
| - | - |
| 2014-04-23 16:45 | 8.140 |


WS06 
-----

* mean hourly change: 0.492
* hourly std: 0.574
* hourly four std + : 2.79
* hourly three std +: 2.21
* hourly median : 0.3 
* hourly max: 8.8

* mean 15-min change: 0.131
* 15-min std: 0.149 
* 15-min four std + : 0.728
* 15-min three std +: 0.579
* 15-min median : 0.087 
* 15-min max: 2.65


WS07
-------

* mean hourly  change: 0.624
* hourly  std: 0.763 
* hourly  four std + : 3.677 
* hourly  three std +: 2.914
* hourly  median : 0.3 
* hourly  max: 9.5

* 15-min change: 0.158
* 15-min std: 0.188
* 15-min four std + : 0.911
* 15-min three std +: 0.722
* 15-min  median : 0.090
* 15-min  max: 2.114

Duplicates with different values 
-------------

| date | value of air T |
| - | - |
| 2012-05-23 00:00 | 3.604|
| 2013-10-24 07:30 | 7.799|
| 2013-10-24 07:30 | 7.840 |
| 2014-10-22 00:30 | 6.856|


WS08 
-----

* mean hourly  change: 0.481
* hourly std: 0.607
* hourly four std + : 2.909
* hourly three std +: 2.302
* hourly median : 0.3 
* hourly max: 7.6


* mean 15-min change: 0.135
* 15-min  std: 0.165
* 15-min  four std + : 0.795 
* 15-min  three std +: 0.630 
* 15-min  median : 0.080 
* 15-min  max: 2.240

Duplicates with different values hourly 
-------------

| date | value of air T |
| - | - |
| 2013-01-01 00:00 | 3.299 |
| 2013-01-23 23:15 | 1.161 |
| 2013-01-23 23:30 | 1.156 |
| 2013-01-23 23:45 | 1.167 |
| 2014-04-30 13:30 | 19.63 |



WS10 
------

* mean hourly change: 0.794
* hourly std: 0.878
* hourly four std + : 4.307
* hourly three std +: 3.429
* hourly median : 0.5 
* hourly max: 7.1

* mean 15-min change: 0.208
* 15-min std: 0.236
* 15-min four std + : 1.155
* 15-min three std +: 0.918 
* 15-min median : 0.130 
* 15-min max: 2.829


Duplicates with different values 
-------------

| date | value of air T |
|-|-|
| 2012-05-08 18:30 | 15.789 |
| 2012-05-08 18:45 | 15.600 |
| 2012-05-08 19:00 | 15.180 |
| 2012-05-08 19:15 | 14.710 |
| 2012-05-08 19:30 | 14.289 |



LOOKOUT 
---------

* mean hourly change: 0.797
* std: 0.921
* four std + : 4.479
* three std +: 3.558
* median : 0.5 
* max: 8.0


TS-LOOKOUT 
----------

* mean hourly change: 0.484 
* std: 0.679
* four std + : 3.202 
* three std +: 2.523 
* median : 0.3 
* max: 8.6

Questionable Changes 
-------------

| date | change in C |
|- | - |
| 2008-08-15 12:00 | 10.1 |
| 2009-07-28 12:00 | 10.4 |


McRae 
--------

* mean hourly change: 0.601 
* std: 0.802 
* four std + : 3.811
* three std +: 3.010 
* median : 0.3 
* max: 9.9


Lower Mcrae 
-----------

* mean hourly change: 0.919
* std: 1.093 
* four std + : 5.292
* three std +: 4.199
* median : 0.5 
* max: 7.3


Mack Creek
----------

* mean hourly change: 0.617 
* std: 0.927
* four std + : 4.327
* three std +: 3.399
* median : 0.3 
* max: 9.7

Questionable Changes 
-------------

| date | change in C |
|- |- |
| 2001-07-11 14:00 | 10.2 |

Lower Mack 
----------

* mean hourly change: 0.663
* std: 0.822
* four std + : 3.955
* three std +: 3.135 
* median : 0.4 
* max: 7.9
