#!/usr/bin/python

import os,sys,re
import datetime,time

if __name__ == '__main__':
   
    stdin_logs = sys.stdin.readlines()
    
    print stdin_logs
    
    for log in stdin_logs:
        
        log = re.sub("\n","",log)
        
        print "next:", log
        
        f = open(log, 'r')
        
        head_line = None
        detail_line = None
        
        # Jan 17, 2013 1:30:02 PM
        timeform = "%b %d, %Y %I:%M:%S %p"
        
        complete_start = None
        complete_stop = None
        
        timestart = None
        timestop = None
        
        total_method_execs = 0
        total_time = 0
        
        for line in f:
            #mtch_obj = re.search(" com.crossview.commerce.dataload.loader.DeltaBusinessObjectLoader execute$",line)
            mtch_obj = re.search(" com.carquest.commerce.dataload.mediator.ACESObjectMediator transform$",line)
            
            if mtch_obj != None:
                head_line = line
                
                #print "head line:", head_line
                
                if timestop == None and timestart == None: 
                    timestart = line[0:mtch_obj.start()]
                    
                    #print "timestart:",timestart
                    
                    timestart = time.strptime(timestart, timeform )
                    
                    if complete_start == None: complete_start = timestart
                    
                    timestart = datetime.datetime(timestart.tm_year, timestart.tm_mon, timestart.tm_mday, hour=timestart.tm_hour,minute=timestart.tm_min,second=timestart.tm_sec)
                    
                    
                    
                    
                if timestop == None and timestart != None:
                    timestop = line[0:mtch_obj.start()]
                    
                    #print "timestop:",timestop
    
                    timestop = time.strptime(timestop, timeform)
                    
                    complete_stop = timestop
                    
                    timestop = datetime.datetime(timestop.tm_year, timestop.tm_mon, timestop.tm_mday, hour=timestop.tm_hour,minute=timestop.tm_min,second=timestop.tm_sec)
                    
                   
            
            if head_line != None and mtch_obj == None: 
                detail_line = line
                
                #print "detail line:", detail_line
                
            if detail_line != None and head_line != None:
                return_mtch_obj = re.search("^FINER: RETURN$",detail_line)
                
                time_diff = timestop- timestart
                
                #print "adding more time:", time_diff
                
                if time_diff.total_seconds() != 0:
                    total_time = total_time + time_diff.total_seconds()
                else:
                    total_time = total_time + 0.5 # one milisecond
                    
                total_method_execs = total_method_execs + 1
                
                timestart = None
                timestop = None
                head_line = None
                detail_line = None
        
        f.close()
               
        
    complete_stop = datetime.datetime(complete_stop.tm_year, complete_stop.tm_mon, complete_stop.tm_mday, hour=complete_stop.tm_hour,minute=complete_stop.tm_min,second=complete_stop.tm_sec)
    complete_start = datetime.datetime(complete_start.tm_year, complete_start.tm_mon, complete_start.tm_mday, hour=complete_start.tm_hour,minute=complete_start.tm_min,second=complete_start.tm_sec)
        
    #print "complete start:", complete_start
    #print "complete stop:", complete_stop
    
    #complete_total = complete_stop - complete_start
    
    #print "complete total time (seconds):", complete_total.total_seconds()
    
    print "total method executions:", total_method_execs
    print "total method time:", total_time
    
    #time_over_execs = complete_total.total_seconds() / total_method_execs
    time_over_execs = total_time / total_method_execs
    
    print "total time over method execs (seconds):", time_over_execs
    
    time_times_millions = 1000000 * time_over_execs
    
    print "total time per million (seconds):", time_times_millions
    
    times_per_millions_hours = time_times_millions / 3600
    
    print "total time per million (hours):", times_per_millions_hours
    
    print "total time for 25 million (hours):", times_per_millions_hours * 25