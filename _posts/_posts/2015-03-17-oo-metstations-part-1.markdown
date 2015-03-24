---
layout: post
title: "OO MetStations, Part 1"
date: 2015-03-17T15:47:47-07:00
---

I have developed a class for analyzing our Benchmark met-stations that I find to be fairly robust, although it is still being worked on. As I am not the best "object oriented" thinker, I am sure that it is not the best code, but I hope that in documenting it here, I can grow and it can grow better, and perhaps we can make it a service for others. 

The class is a class I call "MetStation". MetStation is the parent of subclasses for each benchmark station, because each station has similar links, names of attribtues, etc. MetStation also has a subclass called "MetDatRescue" - this is a general class for things that must be piecemealed together from the METDAT database. I suppose I'll introduce you to this one here, since I'm working on it.

Here's an instance of MetDatRescue, being called:

xtempx is the module which contains the MetStation class. 

        U_rel= xtempx.MetDatRescue("relhum", probe_index, "select TmStamp, rh_450_avg from metdat.dbo.prim_226_table160 where TmStamp > '2013-05-01' and \
                    TmStamp < '2014-05-15' order by TmStamp asc ", datetime.datetime(2013,5,1,0,0), datetime.datetime(2014,05,15,0,0), datetime.timedelta(minutes=60), "primet")
                    U_air = xtempx.MetDatRescue("airtemp", probe_index, "select TmStamp, air_450_avg from metdat.dbo.prim_226_table115 where TmStamp > '2013-05-01' and \
                    TmStamp < '2014-05-15' and datepart(minute, TmStamp) = 0 order by TmStamp asc ", datetime.datetime(2013,5,1,0,0), datetime.datetime(2014,05,15,0,0), datetime.timedelta(minutes=60), "primet")
