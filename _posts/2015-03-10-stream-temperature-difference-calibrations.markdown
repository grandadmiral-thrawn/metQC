---
layout: post
title: "Stream Temperature Difference Calibrations"
date: 2015-03-10T13:04:47-07:00
---

This post details the "difference" thresholds for the stream temperature at H.J.Andrews.

I would suggest to use 0.25 C as the five minute change threshold and 1 C as the hourly change threshold. This should flag a few values which are questionable while leaving most values in place.

Structure
----------

1. hourly bounds and statistics
2. five minute bounds and statistics
3. list of TmStamps in METDAT where the second value for stream temperature is not the same as the first value; usually indicates a case where the first value is erroneous and the second one is a real number.

Ex. of the above, from WS08; PORTAL would display this:

                2012-05-23 15:45:00.0000000     2599    110     4591    2012    144     1545    9.65    9.8     -6999

The actual value is the second in the duplicate series, not displayed on the portal, which is this:

                2012-05-23 15:45:00.0000000     8054    108     2086    2012    144     1545    0.153   0.03385 6.119

4. List of time stamps where the change between two subsequent stream temperatures is more than 3 but less than 10, from the hourly measurements in HT004; indicates an error probably not caused by an error code but a bad measurement or drift.


5. List of time stamps where the change between two subsequent stream temperatures is more than 3 but less than 10, from the five minute measurements in METDAT; indicates an error probably not caused by an error code but a bad measurement or drift.


WS01
------

* mean hourly change: 0.0830 
* std: 0.0923
* four std + : 0.452 
* three std +: 0.360
* median : 0.1 
* max: 2.7

* mean 5-min change: 0.011
* 5 min std: 0.0165
* 5 min four std + : 0.077
* 5 min  three std +: 0.060
* 5 min median : 0.009
* 5 min max: 1.759

WS01 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
| 2012-05-23 16:00 | 9.609 |

Hourly Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
| 2009-01-08 23:00 | questionable changes: 4.6 |
| 2009-01-08 04:00 | questionable changes: 4.5 |



WS02
--------

* mean hourly change: 0.076
* std: 0.088
* four std + : 0.428
* three std +: 0.340 
* median : 0.1 
* max: 2.8

* mean 5-min change: 0.012 
* 5-min std: 0.0304
* 5-min four std + : 0.1337 
* 5-min three std +: 0.1033
* 5-min  median : 0.009 
* 5-min max: 2.969

WS02 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
|  2012-05-08 16:55|10.039|
|  2012-05-08 17:00|10.039|
|  2012-05-08 17:05|10.039|
|  2012-05-08 17:10|10.030|
|  2012-05-08 17:15|10.030|
|  2012-05-08 17:20|10.030|
|  2012-05-08 17:25|10.020|
|  2012-05-08 17:30|10.010|
|  2012-05-08 17:35|10.010|
|  2012-05-08 17:40|10.010|
|  2012-05-08 17:45|10.010|
|  2012-05-08 17:50|10.020|
|  2012-05-22 11:00|9.010 |
|  2014-10-22 00:20|10.590|

* Note on these it appears to be slight differences between each measurement but neither is "unrealistic":


                2012-05-08 16:55:00.0000000     3495    102     3640    2012    129     1655    0.164   0.02879 10.04
                2012-05-08 16:55:00.0000000     3507    102     3640    2012    129     1655    0.163   0.02889 10.03
                2012-05-08 17:00:00.0000000     3496    102     3640    2012    129     1700    0.164   0.02883 10.05
                2012-05-08 17:00:00.0000000     3508    102     3640    2012    129     1700    0.163   0.02875 10.04
                2012-05-08 17:05:00.0000000     3497    102     3640    2012    129     1705    0.164   0.02883 10.05
                2012-05-08 17:05:00.0000000     3509    102     3640    2012    129     1705    0.163   0.02891 10.04


Hourly Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
| 2013-08-08 12:35 | 4.010 |



WS03
-------

* mean hourly change: 0.104
* std: 0.126
* four std + : 0.610 
* three std +: 0.483 
* median : 0.1 
* max: 2.0

* 5-min change: 0.0117 
* 5-min std: 0.0201
* 5-min four std + : 0.0921
* 5-min three std +: 0.0720
* 5-min median : 0.010
* 5-min max: 2.840


WS03 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
|  2012-12-11 14:05| 6.250 |
|  2014-04-22 16:05| 7.659 |
|  2014-04-23 15:40| 15.89 |
|  2014-04-23 16:40| 8.899 |
|  2014-04-23 16:45| 9.039 |
|  2015-02-18 15:10| 7.169 |


Hourly Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
|2014-04-23 12:05| 3.809 | 
|2014-04-23 17:35| 3.250 |
|2014-04-22 15:05| 6.220 |
|2014-04-22 14:05| 8.290 |
|2014-04-23 17:20| 3.799 |
|2014-04-23 15:50| 3.760 |
|2015-01-07 11:25| 4.115 |
|2014-04-22 14:00| 8.779 |
| 2012-12-19 10:45|  3.1|




WS06
----------

* mean hourly change: 0.073
* std: 0.1001
* four std + : 0.477
* three std +: 0.376 
* median : 0.1 
*  max: 3.0

* 5-min change: 0.0115
* 5-min std: 0.0258
* 5-min four std + : 0.115
* 5-min three std +: 0.089
* 5-min median : 0.010
* 5-min  max: 2.313

WS06 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
|  2014-04-30 14:50 | 7.5 |
|  2015-02-19 15:10 | 7.35 |

Five Minute Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
| 2013-08-09 15:10 |3.340 |
| 2012-12-24 11:00 | 3.4 |
| 2012-12-24 11:15 | 3.4 |




WS07
-------

* mean hourly change: 0.079
* std: 0.102
* four std + : 0.486
* three std +: 0.384
* median : 0.1 
* max: 2.7

* mean 5-min change: 0.011 
* 5-min std: 0.025 
* 5-min four std + : 0.111
* 5-min three std +: 0.086
* 5-min median : 0.010
* 5-min max: 2.404

WS07 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
|2012-05-23 16:00| 6.525|
|2013-10-24 07:20| 8.430|
|2013-10-24 07:30| 8.420|
|2014-04-30 11:50| 7.580|

Five Minute Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
| 2014-05-21 11:50| 3.519 |
| 2014-07-15 12:35| 4.359 |
| 2012-05-02 12:55| 3.542 |
| 2014-04-30 11:35| 4.649 |
| 2014-07-15 12:40| 3.909 |
| 2014-05-21 11:45| 3.779 |
| 2012-05-02 12:50| 3.621 |
| 2014-04-30 11:30| 4.810 |




WS08
--------

* mean hourly change: 0.059
* std: 0.094 
* four std + : 0.436
* three std +: 0.342 
*  median : 0.0 
* max: 2.8

* 5-min change: 0.0104
* 5-min std: 0.027
* 5-min four std + : 0.121
* 5-min three std +: 0.093
* 5-min median : 0.010
* 5-min max: 2.883

WS08 Duplicates in METDAT with diff vals
------------------ 

|date | val metdat|
|-|-|
|  2012-05-23 15:45|6.119|
|  2013-01-01 00:00|4.599|
|  2013-01-23 23:05|4.560|
|  2013-01-23 23:10|4.571|
|  2013-01-23 23:15|4.571|
|  2013-01-23 23:20|4.560|
|  2013-01-23 23:25|4.581|
|  2013-01-23 23:30|4.562|
|  2013-01-23 23:35|4.562|
|  2013-01-23 23:40|4.571|
|  2013-01-23 23:45|4.571|
|  2013-01-23 23:50|4.562|
|  2013-01-23 23:55|4.571|
|  2014-03-20 16:35|4.855|
|  2014-04-30 13:30|7.059|

Hourly Stream Temp Change > 3
-------------------------

| date | change | 
|-|-|
|2000-04-10 14:00| 3.1|
|2002-05-12 13:00| 3.2|
|2002-04-04 14:00| 3.2|
|2001-05-06 13:00| 3.1|
|2000-04-30 13:00| 3.2|
|2000-03-31 14:00| 3.2|
|2002-05-08 13:00| 3.4|
|2001-04-25 13:00| 3.1|
|2002-04-03 14:00| 3.1|
|2002-05-11 13:00| 3.3|
|2000-04-07 14:00| 3.3|
|2000-04-20 13:00| 3.1|
|2000-04-29 13:00| 3.1|
|2002-04-24 13:00| 3.2|
|2000-04-02 14:00| 3.3|
|2001-05-07 13:00| 3.3|




WS10 
------

* mean hourly change: 0.192
* std: 0.246
* four std + : 1.179
* three std +: 0.932 
* median : 0.1 
* max: 3.0

* 5-min change: 0.018
* 5-min std: 0.026
* 5-min four std + : 0.123
* 5-min three std +: 0.097
* 5-min median : 0.010 
* 5-min max: 2.819

WS10 Duplicate values in METDAT
------------------ 

|date | val metdat|
|-|-|
|  2012-05-08 18:30|10.829 |
|  2012-05-08 18:35|10.800 |
|  2012-05-08 18:40|10.780 |
|  2012-05-08 18:45|10.730 |
|  2012-05-08 18:50|10.719 |
|  2012-05-08 18:55|10.670 |
|  2012-05-08 19:00|10.649 |
|  2012-05-08 19:05|10.600 |
|  2012-05-08 19:10|10.569 |
|  2012-05-08 19:15|10.519 |
|  2012-05-08 19:20|10.510 |
|  2012-05-08 19:25|10.480 |
|  2012-05-08 19:30|10.430 |
|  2014-08-13 11:50|15.589 |



LOOKOUT 
--------

* mean hourly change: 0.139
* std: 0.189
* four std + : 0.896
* three std +: 0.706
* median : 0.1 
* max: 2.3


TS-LOOKOUT 
-------------

* mean hourly change: 0.052 
* std: 0.075
* four std + : 0.353
* three std +: 0.278
* median : 0.0 
* max: 2.0

McRae 
-------

* mean hourly change: 0.053
* std: 0.085
* four std + : 0.395
* three std +: 0.309
* median : 0.0 
* max: 1.2

Lower Mack
----------

* mean hourly change: 0.613
* std: 0.590
* four std + : 2.972
* three std +: 2.382 
* median : 0.5 
* max: 3.0