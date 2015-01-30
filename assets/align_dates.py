#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymssql
import csv
from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpld3
import datetime
import unicodedata


def get_csv_on_page(link, substring_list):
    """ Go to the link (HTML page), make the CSV path, get the requested columns"""
    csvfile = link.split('.html')[0] + '.csv'
    r = requests.get(csvfile)
    w = r.text.split('\r\n')
    headers = w[2].split(',')

    attr = {}
    """ Get the date column from the csv table"""
    

    for index, item in enumerate(headers):

        if any(substring in str(item) for substring in substring_list) is True:
            attr[str(item).strip('"')] = index
        else:
            pass

    """ create a lookup table containing floats (prefered) or strings (secondary) for the 
    desired attributes from the csv on the web
    """
    val = {}

    for row_index in xrange(5,len(w)-1):
        
        getrow = w[row_index].split(',')
                
        outputs = [getrow[index].strip('"').encode('UTF8') for index in attr.values()]

        """ val is searchable by keys which are the attribute names. i.e. val['Date']"""
        for index, item in enumerate(attr.keys()):
            if item not in val:
                val[item] = []
                try:
                    val[item].append(float(outputs[index]))
                except Exception:
                    val[item].append(str(outputs[index]))
            else:
                try:
                    val[item].append(float(outputs[index]))
                except Exception:
                    val[item].append(str(outputs[index]))
    
    return val

def drange(start, stop, step):
    """ define an interval range over which to iterate
    final arguement can let you iterate with a jump
    that is not 1 (i.e. 10 or 0.4)

    for example:
    thisrange = drange(0.0, 250.0, 0.1)
    here's how to see the whole range
    ranger = [round(x,2) for x in thisrange]
    """
    r = start
    while r < stop:
        yield r
        r+=step

def get_extent_of_data(val):
    """ first and last day of data"""
    first_day = val.values()[0][0]
    last_day = val.values()[0][-1]

    return first_day, last_day

def drange_wrapper(dt1, dt2, dtstep):
    """ 
    drange, but using date-time time-delta for the step, in minutes

    example use:
    map_day = align_dates.drange_wrapper(val.values()[0][0], val.values()[0][-1], 5)
    """
    try: 
        start1 = datetime.datetime.strptime(dt1, '%Y-%m-%d %H:%M:%S')
        stop1 = datetime.datetime.strptime(dt2,'%Y-%m-%d %H:%M:%S')
        step1 = datetime.timedelta(minutes=dtstep)
        return drange(start1, stop1, step1)
    except Exception:
        pass

def comp_dates(val, dtstep, *args):
    """ function will fail when the first date is off"""

    # get the first and last days
    first_day, last_day = get_extent_of_data(val)

    # generate an idealized wrapper
    map_day = drange_wrapper(first_day, last_day, dtstep)
    dt2 = [x for x in map_day]
    # print dt2

    # get the dates that are actually there
    gotten_dates = val.values()[0]

    # convert the dates that actually exist to a date list
    dt1 = [datetime.datetime.strptime(gotten_dates[x],'%Y-%m-%d %H:%M:%S') for x in drange(0, len(gotten_dates)-1, 1)]
    # print dt1

    # find not shared dates-- dt2 should have every single date, dt1 will have only the ones in the data
    not_shared = sorted(set(dt2) - set(dt1))

    print [datetime.datetime.strftime(not_shared[x], '%Y-%m-%d %H:%M:%S') for x in xrange(0, len(not_shared)-1)]   
    
    if not args:
        return not_shared

    elif args:
        outputfile = args[0]
        with open(outputfile,'wb') as writefile:
            writer= csv.writer(writefile, quoting=csv.QUOTE_NONNUMERIC, delimiter = ",")
            writer.writerow(["IDEAL_DATE"])

            human_dates = [datetime.datetime.strftime(dt2[x],'%Y-%m-%d %H:%M:%S') for x in drange(0, len(dt2)-1, 1)]
            for each_date in human_dates:
                writer.writerow([each_date])

        return not_shared

    else:
        return not_shared


if __name__ == "__main__":

    #link = "http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_5min_2014.html"
    #val = get_csv_on_page(link,["Date"])
    #not_shared = comp_dates(val, 5, "ideal_uplmet_227_5min_2012t02014.csv")

    #link = "http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_5min_2013.html"
    #val = get_csv_on_page(link,["Date"])
    #not_shared = comp_dates(val, 5, "ideal_primet_226_5min_2013t02014.csv")

    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_225_5min_2014.html"
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_225_5min_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_5min_2014.html", 
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_5min_2015.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_5min_2013.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_5min_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_5min_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_5min_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_5min_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_5min_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_5min_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_230_a_5min_2014.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_5min_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_5min_2015.html"]
    link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/HI15/data/hi15_207_5min_2013.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VARA/data/varmet_301_a_5min_2014.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VARA/data/varmet_301_a_5min_2015.html"]
    for link in link_list:
        val = get_csv_on_page(link,["DateString"])
        print "doing file at link: %s" %(link)
        not_shared = comp_dates(val, 5)
        del val, not_shared


    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_15min_2013.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_15min_2014.html"
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_15min_2015.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VARA/data/varmet_301_b_15min_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/VARA/data/varmet_301_b_15min_2015.html"]
    link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/HI15/data/hi15_208_15min_2013.html"]
    for link in link_list:
        val = get_csv_on_page(link,["DateString"])
        print "doing file at link: %s" %(link)
        not_shared = comp_dates(val, 15)
        del val, not_shared

    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_225_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_225_hrly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_hrly_2015.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_hrly_2013.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_hrly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_hrly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_hrly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_230_a_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_230_a_hrly_2015.html"]
    #link_list =["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_hrly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_hrly_2015.html"]
    #link_list = []
    #for link in link_list:
    #    val = get_csv_on_page(link,["Date"])
    #    print "doing file at link: %s" %(link)
    #    not_shared = comp_dates(val, 60)
    #   del val, not_shared

    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/CenMet/data/cenmet_233_a_dly_2015.html"]
    #link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_226_a_dly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_a_dly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_229_b_dly_2015.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_230_a_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/PRIMET/data/primet_230_a_dly_2015.html"]
    #link_list =["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_dly_2014.html",
    #"http://andrewsforest.oregonstate.edu/lter/about/weather/portal/UPLMET/data/uplmet_227_dly_2015.html"]
    link_list = ["http://andrewsforest.oregonstate.edu/lter/about/weather/portal/HI15/data/hi15_207_dly_2013.html",
    "http://andrewsforest.oregonstate.edu/lter/about/weather/portal/HI15/data/hi15_208_dly_2013.html"]
    for link in link_list:
        val = get_csv_on_page(link,["DateString"])
        print "doing file at link: %s" %(link)
        not_shared = comp_dates(val, 1440)
        del val, not_shared