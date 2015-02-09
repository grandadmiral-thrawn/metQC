import pymssql
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpld3
import datetime
import tvh
import math

""" A new method for getting the daily data, mins, and maxes, with the option to write .csv if you want"""

def form_connection():
    """
    connects to the METDAT database to gather the data
    returns a cursor
    """

    # the date format is this:
    dateformat='%Y-%m-%d %H:%M:%S'

    # Connect to MSSQL Server
    conn = pymssql.connect(server="stewartia.forestry.oregonstate.edu:1433",
                           user="petersonf",
                           password="D0ntd1sATLGA!!",
                           database="FSDBDATA")

    # Create a database cursor
    cursor = conn.cursor()

    return cursor

def query_data(cursor, *args):

  if not args:
    query = """select year(date_time), month(date_time), \
     day(date_time), probe_code, avg(airtemp_mean) from \
     fsdbdata.dbo.ms04311 group by year(date_time), month(date_time),\
     day(date_time), probe_code order by year(date_time), \
     month(date_time), day(date_time) asc"""  

  elif args[0] == "r":
    query = """select year(date_time), month(date_time), \
     day(date_time), probe_code, avg(relhum_mean) from \
     fsdbdata.dbo.ms04312 group by year(date_time), month(date_time),\
     day(date_time), probe_code order by year(date_time), \
     month(date_time), day(date_time) asc""" 

  elif args[0] == "d":
    query = """select year(date_time), month(date_time), \
     day(date_time), probe_code, avg(dewpt_mean) from \
     fsdbdata.dbo.ms04317 group by year(date_time), month(date_time),\
     day(date_time), probe_code order by year(date_time), \
     month(date_time), day(date_time) asc""" 

  elif args[0] == "v":
    query = """select year(date_time), month(date_time), \
     day(date_time), probe_code, avg(vpd_mean) from \
     fsdbdata.dbo.ms04318 group by year(date_time), month(date_time),\
     day(date_time), probe_code order by year(date_time), \
     month(date_time), day(date_time) asc""" 

  elif args[0] == "p":
    query = """select year(date_time), month(date_time), \
     day(date_time), probe_code, avg(vap_mean) from \
     fsdbdata.dbo.ms04318 group by year(date_time), month(date_time),\
     day(date_time), probe_code order by year(date_time), \
     month(date_time), day(date_time) asc"""


  else: 
    print """that is not airtemp(blank), wind('w'), 
    dewpoint('d'), vpd('v'), vaporpressure('p')
    or relhum('r')"""

  cursor.execute(query)

  output_dictionary = {}
    
  for row in cursor:
      
      print row
      year = int(row[0])
      month = int(row[1])
      day = int(row[2])
      probecode = str(row[3])

      try:
          attr = float(row[4])
      except Exception:
          attr = str(row[4])

      dtstamp = datetime.datetime.strptime(str(row[5]),'%Y-%m-%d %H:%M:%S')

      if probecode not in output_dictionary:
          output_dictionary[probecode] = [{year:{month:{day:(dtstamp, attr)}}}]
      elif year in output_dictionary:

          output_dictionary[probecode].append({year:{month:{day:(dtstamp, attr)}}})

  return output_dictionary

  def check_tarh(ta, rh):
    
    ta = tvh.fix2(ta)
    rh = tvh.fix(rh)
    svap = tvh.satvp(ta)
    td = tvh.dewpt(svap, rh)
    vap = tvh.vaporp(rh, svap)

    return ta, rh, svap, td, vap
