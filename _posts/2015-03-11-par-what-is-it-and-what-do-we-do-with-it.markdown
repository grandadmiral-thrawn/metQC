---
layout: post
title: "PAR- What Is It and What Do We Do With It?"
date: 2015-03-11T08:26:21-07:00
---

PAR is a measurement of photosynthetically active radiation. It is measured in units of micro-mols of photons per meters squared per second. The basic principle is that organisms mostly use light in the 400-700 nm wavelengths, and so PAR can be used to look at factors such as oxygen usage and carbon uptake. 

Better descriptions are found [here](http://www.fondriest.com/environmental-measurements/parameters/weather/photosynthetically-active-radiation/)

and [here](http://agi32.com/blog/2014/12/10/photometry-and-photosynthesis)

We measure part with an LI190SB, a LiCOR instrument attached to a Campbell logging platform. Briefly, a diode is excited differently by different wavelengths of light, and the instrument uses the difference to the re-grounding of the instrument voltage to figure out the number of excitations in certain bins corresponding to certain wavelengths over a sampling period. Then it performs an integration, resulting in a net amount of energy over that time period and representative area. Because the energy is quantized in the form of photons, the energy is represented in micro-mols. There is another method representing the energy in terms of total energy gyield but it has been suggested this is not the best for outdoor environments. See [here](http://upload.wikimedia.org/wikipedia/commons/f/f8/Photosynthesis_yield_photon_flux_spectral_weighting.svg).

* Campbell says that the *MAXIMUM BOUND* for this system should be *2000 micromols per meters per second squared*

* Realistically, the *MINIMUM BOUND* is 0. However, Campbell acknowledges that at night fall, 1 % errors can occur, so even stretching this to -10 to -50 as acceptable in a certain hour range would be appropriate.

* For computing more specific bounds, I questioned if we could trust the historical values to be consistent since they had very high deviation due to cloudiness and the nature of PAR measurements. I built a system to test different data subsets. See an example of the results at the bottom. 


Here are monthly PAR means by hour (i.e. January, all 13:00 hours, mean PAR value - so the mean of 31 points.)

        MONTH, HOUR, MEAN PAR
        1, 0, 0.000000
        1, 1, 0.000000
        1, 2, 0.000467
        1, 3, 0.000000
        1, 4, 0.000000
        1, 5, 0.000934
        1, 6, 0.000934
        1, 7, 1.021495
        1, 8, 27.324766
        1, 9, 76.509583
        1, 10, 211.285914
        1, 11, 326.702197
        1, 12, 362.049579
        1, 13, 340.542776
        1, 14, 263.985514
        1, 15, 142.247196
        1, 16, 37.632291
        1, 17, 2.413439
        1, 18, 0.000000
        1, 19, 0.000000
        1, 20, 0.000000
        1, 21, 0.000000
        1, 22, 0.000000
        1, 23, 0.000000
        2, 0, 0.000000
        2, 1, 0.000000
        2, 2, 0.000000
        2, 3, 0.000000
        2, 4, 0.000000
        2, 5, 0.000000
        2, 6, 0.025197
        2, 7, 10.610177
        2, 8, 60.859189
        2, 9, 123.997035
        2, 10, 350.020256
        2, 11, 474.059317
        2, 12, 513.451485
        2, 13, 493.399009
        2, 14, 414.171287
        2, 15, 278.189108
        2, 16, 101.037128
        2, 17, 21.329207
        2, 18, 0.255445
        2, 19, 0.000000
        2, 20, 0.000000
        2, 21, 0.000000
        2, 22, 0.000000
        2, 23, 0.000000
        3, 0, 0.009962
        3, 1, 0.009487
        3, 2, 0.008064
        3, 3, 0.006166
        3, 4, 0.005692
        3, 5, 0.011865
        3, 6, 6.766603
        3, 7, 52.789373
        3, 8, 124.103415
        3, 9, 310.137571
        3, 10, 539.467267
        3, 11, 643.046015
        3, 12, 689.612903
        3, 13, 645.349146
        3, 14, 549.674098
        3, 15, 405.914136
        3, 16, 224.490986
        3, 17, 73.457779
        3, 18, 7.985294
        3, 19, 0.008064
        3, 20, 0.008064
        3, 21, 0.008538
        3, 22, 0.011859
        3, 23, 0.011385
        4, 0, 0.000000
        4, 1, 0.000000
        4, 2, 0.000000
        4, 3, 0.000000
        4, 4, 0.000000
        4, 5, 4.981862
        4, 6, 46.654411
        4, 7, 115.080882
        4, 8, 275.911274
        4, 9, 586.588235
        4, 10, 756.637745
        4, 11, 869.793510
        4, 12, 887.401182
        4, 13, 832.417365
        4, 14, 712.191060
        4, 15, 550.217156
        4, 16, 350.734313
        4, 17, 132.525000
        4, 18, 38.812745
        4, 19, 1.629901
        4, 20, 0.000000
        4, 21, 0.000000
        4, 22, 0.000000
        4, 23, 0.000000
        5, 0, 0.007115
        5, 1, 0.004743
        5, 2, 0.004269
        5, 3, 0.004269
        5, 4, 0.916982
        5, 5, 27.047912
        5, 6, 86.399430
        5, 7, 180.257115
        5, 8, 515.421252
        5, 9, 742.210726
        5, 10, 913.684009
        5, 11, 1000.048768
        5, 12, 1007.612997
        5, 13, 967.554054
        5, 14, 854.186400
        5, 15, 698.504269
        5, 16, 497.701236
        5, 17, 247.793152
        5, 18, 94.497623
        5, 19, 15.421102
        5, 20, 0.086460
        5, 21, 0.004743
        5, 22, 0.006641
        5, 23, 0.007590
        6, 0, 0.000000
        6, 1, 0.000000
        6, 2, 0.000000
        6, 3, 0.000000
        6, 4, 3.496078
        6, 5, 40.473039
        6, 6, 99.453921
        6, 7, 287.058823
        6, 8, 658.319117
        6, 9, 887.681394
        6, 10, 1070.173200
        6, 11, 1188.073146
        6, 12, 1208.214321
        6, 13, 1154.054917
        6, 14, 1046.713580
        6, 15, 875.484551
        6, 16, 664.824509
        6, 17, 394.343627
        6, 18, 148.468627
        6, 19, 37.997054
        6, 20, 1.509073
        6, 21, 0.000000
        6, 22, 0.000000
        6, 23, 0.000000
        7, 0, 0.000000
        7, 1, 0.000000
        7, 2, 0.000000
        7, 3, 0.000000
        7, 4, 1.569259
        7, 5, 35.359108
        7, 6, 88.584440
        7, 7, 190.775142
        7, 8, 795.287001
        7, 9, 1108.239791
        7, 10, 1344.040630
        7, 11, 1492.088320
        7, 12, 1531.805125
        7, 13, 1481.436837
        7, 14, 1349.721639
        7, 15, 1143.416152
        7, 16, 860.872865
        7, 17, 453.149905
        7, 18, 182.265180
        7, 19, 40.437114
        7, 20, 1.286663
        7, 21, 0.000000
        7, 22, 0.000000
        7, 23, 0.000000
        8, 0, 0.000000
        8, 1, 0.000000
        8, 2, 0.000000
        8, 3, 0.000000
        8, 4, 0.005695
        8, 5, 12.603415
        8, 6, 67.959203
        8, 7, 123.169435
        8, 8, 470.225913
        8, 9, 1014.689278
        8, 10, 1237.041330
        8, 11, 1388.377915
        8, 12, 1447.575786
        8, 13, 1387.169919
        8, 14, 1235.025641
        8, 15, 997.226235
        8, 16, 680.271476
        8, 17, 235.161764
        8, 18, 83.202561
        8, 19, 10.907925
        8, 20, 0.010441
        8, 21, 0.000000
        8, 22, 0.000000
        8, 23, 0.000000
        9, 0, 0.000000
        9, 1, 0.000000
        9, 2, 0.000000
        9, 3, 0.000000
        9, 4, 0.000000
        9, 5, 0.854965
        9, 6, 32.117444
        9, 7, 89.571147
        9, 8, 165.326440
        9, 9, 735.402852
        9, 10, 996.433906
        9, 11, 1120.300147
        9, 12, 1159.076581
        9, 13, 1088.642751
        9, 14, 936.755402
        9, 15, 715.401474
        9, 16, 416.031988
        9, 17, 104.994597
        9, 18, 19.798918
        9, 19, 1.019174
        9, 20, 0.043285
        9, 21, 0.000000
        9, 22, 0.000000
        9, 23, 0.000000
        10, 0, 0.000000
        10, 1, 0.000000
        10, 2, 0.000000
        10, 3, 0.000000
        10, 4, 0.000000
        10, 5, 0.000000
        10, 6, 5.517928
        10, 7, 48.126494
        10, 8, 103.211365
        10, 9, 325.694721
        10, 10, 609.359561
        10, 11, 703.253984
        10, 12, 722.810756
        10, 13, 665.792123
        10, 14, 531.389526
        10, 15, 284.119760
        10, 16, 103.142215
        10, 17, 17.250998
        10, 18, 0.122255
        10, 19, 0.000000
        10, 20, 0.000000
        10, 21, 0.000000
        10, 22, 0.000000
        10, 23, 0.000000
        11, 0, 0.000000
        11, 1, 0.000000
        11, 2, 0.000000
        11, 3, 0.000000
        11, 4, 0.000000
        11, 5, 0.000000
        11, 6, 0.060216
        11, 7, 11.282552
        11, 8, 54.381172
        11, 9, 126.465774
        11, 10, 299.769943
        11, 11, 365.464506
        11, 12, 378.422760
        11, 13, 331.560862
        11, 14, 231.111740
        11, 15, 110.402363
        11, 16, 21.381416
        11, 17, 0.402157
        11, 18, 0.000000
        11, 19, 0.000000
        11, 20, 0.000000
        11, 21, 0.000000
        11, 22, 0.000000
        11, 23, 0.000000
        12, 0, 0.009492
        12, 1, 0.009487
        12, 2, 0.009492
        12, 3, 0.009487
        12, 4, 0.009487
        12, 5, 0.007590
        12, 6, 0.007590
        12, 7, 1.272554
        12, 8, 26.639943
        12, 9, 71.850094
        12, 10, 201.994307
        12, 11, 280.879981
        12, 12, 299.161290
        12, 13, 272.254510
        12, 14, 182.747508
        12, 15, 86.729601
        12, 16, 13.759962
        12, 17, 0.037476
        12, 18, 0.000000
        12, 19, 0.000000
        12, 20, 0.000000
        12, 21, 0.001897
        12, 22, 0.009013
        12, 23, 0.008538

Because PAR is not temperature, and is in fact somewhat dependant on cloud cover, I thought it would be important to not blindly trust that annual and diel cycles could be reflected over all site history. So, I did the following:

1. Randomly selected 80 % of the years as one set (from the 1990's through current)
2. Pulled out the remainder of years as a second set. 
3. Computed a mean and difference in means between the two sets using the more detailed "moving window" approach we often use. That is, a moving window of 30 days, for each hour of a day, centered on the middle day.



I'll just show here an example of how values could differ between subsets:

Here is a time in May 10-27th, at hour 8, when the difference between two randomly selected subset means in PAR could be up to 60. From the previous table the mean of all data sets at this hour in May is 515.421252, so that's about a 10 percent difference depending on what year is chosen. 

| MONTH, DAY | HOUR | DIFFERENCE IN MEAN |
| - | - |-|
| (5, 10) | 8 | 18.19 |
| (5, 11) | 8 | 19.41 |
| (5, 12) | 8 | 13.72 |
| (5, 13) | 8 | 14.55 |
| (5, 14) | 8 | 17.1 |
| (5, 15) | 8 | 15.37 |
| (5, 16) | 8 | 27.97 |
| (5, 17) | 8 | 36.3 |
| (5, 18) | 8 | 35.46 |
| (5, 19) | 8 | 47.96 |
| (5, 20) | 8 | 58.88 |
| (5, 21) | 8 | 58.09 |
| (5, 22) | 8 | 56.18 |
| (5, 23) | 8 | 58.33 |
| (5, 24) | 8 | 50.33 |
| (5, 25) | 8 | 40.18 |
| (5, 26) | 8 | 33.46 |
| (5, 27) | 8 | 27.23 |


Here is similar magnitude differences on that same range with a different randomly selected subset:

| MONTH, DAY | HOUR | DIFFERENCE IN MEAN |
| - | - |-|
| (5, 10) | 8 | 57.58 |
| (5, 11) | 8 | 68.73 |
| (5, 12) | 8 | 85.84 |
| (5, 13) | 8 | 91.26 |
| (5, 14) | 8 | 96.0 |
| (5, 15) | 8 | 96.63 |
| (5, 16) | 8 | 97.65 |
| (5, 17) | 8 | 97.79 |
| (5, 18) | 8 | 86.74 |
| (5, 19) | 8 | 81.05 |
| (5, 20) | 8 | 75.66 |
| (5, 21) | 8 | 67.01 |
| (5, 22) | 8 | 65.84 |
| (5, 23) | 8 | 60.48 |
| (5, 24) | 8 | 59.46 |
| (5, 25) | 8 | 61.81 |
| (5, 26) | 8 | 71.95 |
| (5, 27) | 8 | 78.48 |
