---
layout: post
title: "Easy Pre and Me: How to Review an Easy Pre Output"
date: 2015-03-18T15:05:15-07:00
---

DESCRIPTION
----------

The "easypre" precipitation program uses the high-resolution height of the rain gages at CENMET, UPLMET, VANMET, CS2MET, and H15MET to compute precipitation. This is a better method than using the difference between subsequent measurements because often the gage height will show variability that does not indicate a real event. One approach to determining precipitation in the past was to only record positive changes in gage height. This is problematic because evaporation may cause the baseline gage height to decrease so that no positive inputs are counted. Another approach is to count only positive changes, relative to a decreasing baseline, however, in the dry summer months these positive changes are not real, and cause the appearance of rain when in fact there is none. Easypre uses a "state machine" approach. Basically, the gage is either in a "raining" or "not raining" state. When it is in the raining state, only positive fluxes are counted. When it is in the not-raining state, neither positive nor negative fluxes are counted. In both states, the baseline height of the gage is tracked. We then tuned the transitions between the two states to best capture sudden rain events and long dry downs, as well as to acknowledge when gage resets occur, or when a sudden influx from a snow "bomb" occurs. In general the model works fairly robustly, however, the transition into the raining state can be delayed for up to about an hour. This is because a certain, small amount of precipitation must accumulate within a limited time before the state changes. At the change, the accumulated precip from the transitional period is given back to the system. We check these values, which are flagged, manually, to determine if the influx of precipitation needs to be spread back over the past few intervals. In most cases, it does not. We find that this limited manual checking is far better than allowing sudden, erroneous events, such as sloshing, snow bombs, etc. to be allowed to sneak into the data were the state allowed to immediately flip.

To better explore the "easypre" output, I am including in this post a few of the dates/data I scrutinized from the 2014-2015 year outputs from the VANMET sheltered gage and the H15MET gage. In most cases, it is apparent exactly what the flags showed.

VANMET SHELTERED GAGE
-----------------

I will show only key examples here

The layout is like an MS04313 file, with the rightmost five columns showing our calculated precipitation, our flag, the baseline height of the gage, the flag which is delivered on Portal, and the event code. Descriptions I give are in bullets, data is in boxes.

* Here is an example of a well-behaving line

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/13/2014 2:40,0.38,A,45.55,,NA



* Here is an example of a program switch to rainy mode. I moved the increase back into the previous measurement and beyond to match the increase on the gage

    * Before:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:35,0.0,Ae,175,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:40,1.0,Q,175.2,,INTPRO
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:45,0.8,A,176,,NA

    * After:
    
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:35,0.8,Ae,175,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:40,0.2,Q,175.2,,INTPRO
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/20/2014 21:45,0.8,A,176,,NA
        

* Here is an example of a maintance event, when the gage drops a lot. We set the precipitation to 0 and mark it as an estimated ("E") value

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/23/2014 13:30,0,A,280,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/23/2014 13:35,0,A,280.1,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/23/2014 13:40,0,E,31.61,R,MAINTE
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/23/2014 13:45,0,A,31.61,,NA
        

* When the value comes off of many NaN's in a row, we need to change it to remember the original gage height. We flag as a "Q" and make sure that the first difference is 0 (since we do not know where it came from). Notice how "portal" flags this as a reset; this may be incorrect, or at least a different meaning of reset than we associate with the draining of the gage.

    Before:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:45, NaN,M, NaN,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:50,92.25,Q,135.1,R,INTPRO
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:55,0,A,135.1,,NA

    After:
        
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:45, NaN,M, NaN,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:50,0,Q,135.1,R,INTPRO
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,12/29/2014 11:55,0,A,135.1,,NA


        
* Here is an example of, when a maintenance is about to occur, a small increase happens beforehand. This is probably just a person who has their hands in the gage. In this case, I removed the 1.0 precipitation input.

    Before:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 15:10,0,A,32.61,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 15:15,0.46,A,33.11,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 15:20,1,A,34.11,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 15:25,0.25,A,34.36,,NA

    After:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 11:45,0,A,151.8,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 11:50,0,A,152.8,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 11:55,0,E,32.65,R,MAINTE
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/12/2015 12:00,0,A,32.64,,NA
        
        
* Contrast the above to when a 1 increase could actually be a sudden rain event:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/15/2015 17:05,0,Ae,38.98,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/15/2015 17:10,0.87,A,38.85,,INTPRO
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/15/2015 17:15,0.13,A,38.98,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/15/2015 17:20,0,A,38.85,,NA
        
* Maintenance events in our system are triggered by a drop of either a power of ten or 10 mm, whichever is precedent. In this case, maintenance was not triggered on the first drop because it was both less than a power of 10 (about 15mm) and less than 10. I just add one more maintenance flag.


    Before:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:20,0,Ae,152.8,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:25,0,Ae,143.7,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:30,0,E,30.84,R,MAINTE
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:35,0,Ae,30.72,,NA
        
    After:

        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:20,0,Ae,152.8,,NA
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:25,0,Ae,143.7,,MAINTE
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:30,0,E,30.84,R,MAINTE
        MS043,13,VANMET,PPT017,455,1P,PPTVAN01,1/26/2015 15:35,0,Ae,30.72,,NA
        
H15MET gage
--------


There were many fun events on the H15met gage to explore this year. Most are covered in the examples above, but here are a few more. 


* Sometimes the logger just inserts an extra digit. Here's what it looks like BEFORE:

        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:20,0.13,A,388.82,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:25,0,A,388.82,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:30,3500.17,Bomb,3888.99,,WEATHR
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:35,0,E,388.95,,MAINTE
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:40,0.05,A,389,,NA


* obviously that is not a real bomb, but it is easy to fix. You can see that the baseline value simply has one too many points to the left of the decimal, so we "know" what the real value should be. Add in "E" flags for estimated value, and a QUALTY (quality) code. Here's what the above looks like AFTER:


        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:20,0.13,A,388.82,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:25,0,A,388.82,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:30,0.13,E,388.95,,QUALTY
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:35,0,E,388.95,,QUALTY
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,1/12/2014 19:40,0.05,A,389,,NA

* A maintenance behavior sometimes shown is the "slosh", where the post-maintenance baseline is too low for one measurement. It can be zeroed with an "E". Here's an example:

    Before:

        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:10,0,A,553.31,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:15,0.08,A,553.95,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:20,0,E,221.2,,MAINTE
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:25,16.34,A,237.54,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:30,0,A,237.54,,NA

    After:    

        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:10,0,A,553.31,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:15,0.08,A,553.95,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:20,0,E,221.2,,MAINTE
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:25,0,E,237.54,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/17/2014 14:30,0,A,237.54,,NA

* This one is a strange mystery. I do not know what it is. I suspect snow? I left this one in so we could discuss it. This is why checking your data is important. See how the value of baseline goes down by 7, up by 24, up by 17, and then it remains in the low 300's for a while... it is very strange.

        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:15,0,A,267.94,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:20,0,E,260.32,,MAINTE
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:25,23.95,A,284.28,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:30,17.17,Bomb,301.45,,WEATHR
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:35,0.13,A,301.57,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,12/4/2014 12:40,0,A,301.45,,NA

* As a comparison a normal snow bomb looks like this:

        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/9/2014 3:50,0.25,A,454.84,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/9/2014 3:55,0.25,A,455.09,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/9/2014 4:00,4.09,Bomb,459.18,,WEATHR
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/9/2014 4:05,0.25,A,459.44,,NA
        MS043,13,H15MET,PPT013,410,1P,PPTH1501,3/9/2014 4:10,0.38,A,459.82,,NA

