---
layout: post
title: "Snow Pillow at Varamet Calibration"
date: 2015-02-27T09:10:31-08:00
---

VARAMET SNOW PILLOW CALIBRATION
------------


We thought it would be easy to use weights to do a snow-pillow calibration on VARAMET.

<iframe src="http://bl.ocks.org/dataRonin/raw/b7438ef11869be0f63b2" width="700" height="900" frameBorder="0" scrolling="no"></iframe>

The results are that we have 0.99 R-squared value and a calibration setting of:

### SWE(mm) = 0.3821 Liters H20 - 1.404


However, this made a few assumptions... that we could mimic how much snow was actually landing on the pillow, and that the SWE output data we had was right. Turns out these assumptions were wrong.


After a full day of analysis, we have noticed that there are huge discrepancies between the data we have received following processing from both VARAMET and CENMET and the original data logged in METDAT and in the dat files. This is where we are stopped for now. 

I note here how important it is that we put in a flag for SWE > SNOWDEPTH is NOT OKAY. There cannot be more water equivalence than there is snow, unless it's snowing tungsten. 