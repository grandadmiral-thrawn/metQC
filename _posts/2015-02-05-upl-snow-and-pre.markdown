---
layout: post
title: "UPLMET Snowmelt Lysimeter and Precipitation, part 1"
date: 2015-02-05T11:15:31-08:00
---

# Table of Contents
  * [The Problem](#qlink)
  * [The Approach](#approach)
  * [Jump Right To Images](#images)

## See other posts!

[SWE and SNOW-MELT at H15MET](http://dataronin.github.io/metQC/2015/02/12/swe-and-sno.html)

[UPDATES on SNOW-MELT and SWE on UPLMET, H15MET, and CENMET](http://dataronin.github.io/metQC/2015/02/12/updates-on-snow-lysimeter-and-precipitation-on-uplmet-cenmet-and-h15met.html)

[Cumulative precipitation (rain and snow!) on UPLMET, H15MET, and CENMET](http://dataronin.github.io/metQC/2015/02/18/cumulative-precipitation-on-uplmet.html)

[Flags currently used on Portal for UPLMET, H15MET, and CENMET](http://dataronin.github.io/metQC/2015/02/20/notes-on-5-minute-precip-gage-flags.html)

[Adventures in VARAMET Pillow Calibration](http://dataronin.github.io/metQC/2015/02/27/snow-pillow-at-varamet-calibration.html)

## The Problem<a id="qlink"></a>

The recent snowfall as counted by the snow lysimeter on UPLMET seems too be way too much for the site and given its past history. Most of our stands look like they get around 2000-2200 mm total precipitation over the year. We expect that at the end of the water year, the snow and the precipitation will "even out". As the snow melts, they lysimeter will catch up to the rain gauge. As it stands, the history of snow in millimeters on UPLMET (here just showing from 2004 on) is: 

| YEAR | on UPLMET | on CENMET |
| --- | ---|
|2004 |  1290.9 |  1310.1 |
|2005 | 1613.9 | 1518.4 |
|2006 | 1611.9 | 1712.9 |
|2007 |  2152.0 | 1785.1 |
|2008 |   1804.9 | 1259.4 |
|2009 |  1950.0 | 2037.6 |
|2010 |  1781.0 | 2418.6 |
|2011 |  1663.6 | 1463.9 |
|2012 |  2796.1 | 2234.2 |
|2013 |  2240.2 | 1063.7 |
|2014  | 3885.5 | 2672.6 |

So this most recent year is a lot more than the previous, and more than the comparison station.

## The Approach <a id="approach"></a>

With this in mind, we wanted to look at the UPLMET data in comparison to the precipitation from the same years. The approach was to gather and synchronize sums of monthly precipitation for both sites, CENMET and UPLMET, and graph them concurrently. Although UPLMET is of a higher altitude, we expected that it would see similar total preciptiation, although with a different distribution.

To gather the data, simple queries are excuted against MS04303 and MS04309 (FSDBDATA databases) to select and sum (aggregate) the data. This data has already undergone quality control.

## Resulting images<a id="images"></a>

The images below not only show that I am terrible at Javascript, but also that UPLMET receives much more of its precipitation as snow, and that this precipitation appears to be "over-caught" by the gage. We decided to align the gage in the field.


The first and second graphs are blue for snow, red for one of the precipitation gages, and green for the other. The first graph is UPLMET. The second graph is CENMET.


<iframe src="http://bl.ocks.org/dataRonin/03d5507c3ee02736181c" width="700" height="900" frameBorder="0" scrolling="yes"></iframe>

<iframe src="http://bl.ocks.org/dataRonin/a34b7bbdad4499fa3590" width="700" height="900" frameBorder="0" scrolling="yes"></iframe>


SWE is "snow water equivalance" -- that is, for the snow on the ground, if it were perfectly dense water, how deep would it be. Obviously not as deep as the snow. We think these graphs are good when the SWE is high right proceeding when the snow-melt is high, indicating that there was a lot of snow on the ground, and then it melted. This graph depicts that happening as expected.

<iframe src = "http://bl.ocks.org/dataRonin/6264774a683897517d86" width = "700" height = "900" frameBorder = "0" scrolling = "yes"></iframe>
