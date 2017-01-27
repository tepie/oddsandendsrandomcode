#!/usr/bin/python

import os,sys,re
import datetime,time

if __name__ == '__main__':
   # Jan 17, 2013 1:30:02 PM
    timeform = "%b %d, %Y %H:%M:%S"
    timeinputstr = "Dec 01, 9999 23:59:59"
    timeinput = time.strptime(timeinputstr, timeform)
    print timeinput.tm_wday