#!/usr/bin/python
import sys
import csv
from operator import itemgetter


reader = csv.reader(sys.stdin, delimiter='\t')
reader.next() # skip first line containing headers (for local use only)

for line in reader:
    # parse
    #userid, placeid, datetime, lat, lon, city, category= line
     userid, placeid, city, category= line
    
     print '%s\t%s' % (userid, placeid)

