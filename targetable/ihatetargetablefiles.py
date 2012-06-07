#!/usr/bin/python

import os,sys,re,difflib

if __name__ == '__main__':
    
    stdin_targetables = sys.stdin.readlines()
    
    env_groups = {}
    file_groups = {}
    
    for targetable in stdin_targetables:
        #sys.stdout.write("%s" % targetable)
        
        targetable = re.sub("\n","",targetable)
        basename = re.split("/",targetable)[-1]
        
        #sys.stdout.write("%s\n" % basename)
        
        mtch_obj = re.search("\.targetable\.\S+\.",basename)

        env = basename[mtch_obj.start():mtch_obj.end()]
        file_minus = "%s.%s" % (basename[0:mtch_obj.start()], basename[mtch_obj.end():])
        
        #sys.stdout.write("%s, %s\n" % (mtch_obj,env))
        
        env = re.split("\.",env)[-2] 
        
        sys.stdout.write("%s\n" % (env))
        sys.stdout.write("%s\n" % (file_minus))
        
        if not env_groups.has_key(env):
            env_groups[env] = []
            
        if not file_groups.has_key(file_minus):
            file_groups[file_minus] = []
            
        env_groups[env].append(targetable)
        file_groups[file_minus].append(targetable)
        
    
    file_groups_details = {}
    
    for k,v in file_groups.iteritems():
        sys.stdout.write("%s, %s\n" % (k,v))
        
        if not file_groups_details.has_key(k):
            file_groups_details[k] = {}
        
        file_groups_details[k]["file_list_length"] = len(v)
        
        last_file_content = None
        last_file_name = None   
        
        for file in v:
            f = open(file, 'r')
            content = f.readlines()
            f.close()
            
            file_groups_details[k][file] = content
            
            if not last_file_content == None:
                for line in difflib.unified_diff(last_file_content, content, fromfile=last_file_name, tofile=file):
                    sys.stdout.write(line)  
                
            last_file_content = content
            last_file_name = file
            