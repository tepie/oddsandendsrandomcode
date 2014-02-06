#!/usr/bin/python

#svn log -v -r {2014-01-28}:{2014-02-06} . | python svnlogrevisionviajira.py

import sys, re, time

if __name__ == '__main__':

    current_log_record = None
    current_revision = None
    current_comment = None
    
    jira_to_revision = {}
    
    for line in sys.stdin:
     
        # record start: r5792 |
        # record stop: ------------------------------------------------------------------------\n
        # jira comment line fore stop
        
        revision_record = re.match("^r\d+\ \|", line)
        stop_record = re.match("^\-+$",line)
        
        if revision_record != None:
            current_log_record = []
            current_log_record.append(line)
            
            current_revision = re.split(" \|",line)[0][1:]
            
            #sys.stderr.write("current_revision = %s\n" % current_revision)
            
        elif stop_record != None and current_log_record != None:
            
            current_comment = current_log_record[-1]
            
            #sys.stderr.write("current_comment = %s\n" % current_comment)
            
            current_log_record.append(line)
            
            #sys.stderr.write("complete record = %s\n" % current_log_record)
            
            current_log_record = None
            
            commment_jiras = re.findall("[A-Z]{3,}-\d+",current_comment)
            
            for jira in commment_jiras:
                if not jira_to_revision.has_key(jira):
                     jira_to_revision[jira] = []
                     
                jira_to_revision[jira].append(current_revision)
            
        elif current_log_record != None:
            current_log_record.append(line)
            
            
    #sys.stderr.write("jira_to_revision = %s\n" % jira_to_revision)   
    for k, v in jira_to_revision.iteritems():
        v.sort()
        
        log_command = "svn log "
        
        for jira in v: 
            log_command = log_command + "-r " + jira + " "
            
        log_command = log_command + " --diff > " + k + ".diff"
        
        sys.stdout.write("%s\n" % log_command)

            