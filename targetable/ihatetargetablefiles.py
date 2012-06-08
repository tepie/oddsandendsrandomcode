#!/usr/bin/python

import os,sys,re,difflib
import env_mapkeys

#env_groups = {}
file_groups = {}
file_groups_details = {}
file_contents_perenv = {}
file_diffs_perenv = []

def read_targetables(targetables):

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
        
        #sys.stdout.write("%s\n" % (env))
        #sys.stdout.write("%s\n" % (file_minus))
        
        #if not env_groups.has_key(env):
        #    env_groups[env] = []
            
        if not file_groups.has_key(file_minus):
            file_groups[file_minus] = []
            
        #env_groups[env].append(targetable)
        file_groups[file_minus].append(targetable)
        
def readcontentof_targetables():
    for k,v in file_groups.iteritems():
        #sys.stderr.write("%s, %s\n" % (k,v))
        
        if not file_groups_details.has_key(k):
            file_groups_details[k] = {}
        
        #file_groups_details[k]["file_list_length"] = len(v)
        #file_groups_details[k]["file_differences"] = []
        
        last_file_content = None
        last_file_name = None   
        
        for file in v:
            f = open(file, 'r')
            content = f.readlines()
            f.close()
            
            basename = re.split("/",file)[-1]
            mtch_obj = re.search("\.targetable\.\S+\.",basename)

            env = basename[mtch_obj.start():mtch_obj.end()]
            
            env = re.sub("\.targetable\.","",env)
            env = env[:-1]
            
            if not file_contents_perenv.has_key(env):
                file_contents_perenv[env] = {}
            
            file_contents_perenv[env][basename] = content
            
def organize_targetable_content():
    
    for k,v in file_contents_perenv.iteritems():
        sys.stderr.write("%s --> %s\n" % (k,v.keys() ))  
        
    for a in env_mapkeys.ENV_MAPKEYS.keys():
        try:
            b = env_mapkeys.ENV_MAPKEYS[a]
            sys.stderr.write("%s --> %s\n" % (a,b ))  
            
            a_files = file_contents_perenv[a]
            b_files = file_contents_perenv[b]
            
            for af in a_files.keys():
                sub_env = re.sub("\.%s\." % a,".%s." % b, af)
                sys.stderr.write("%s --> %s \n" % (af,sub_env))  
                
                left_contents = a_files[af]
                right_contents = b_files[sub_env]
                
                #diff = difflib.unified_diff(left_contents, left_contents, fromfile=af, tofile=sub_env)
                diff = difflib.HtmlDiff(wrapcolumn=80).make_table(left_contents,right_contents,fromdesc=af, todesc=sub_env,context=True)
                
                file_diffs_perenv.append(diff)
            
            sys.stderr.write("%s \n" % (a_files.keys() )) 
        except KeyError, e:
            sys.stderr.write("environment mapping missing completely for %s\n" % (a))
            file_diffs_perenv.append("<h1>environment mapping missing completely for %s</h1>\n" % (a))


def outputdiff_ashtml():
    sys.stdout.write('''<html><head>
        <style type="text/css">
            table.diff {font-family:Courier; border:medium;}
            .diff_header {background-color:#e0e0e0}
            td.diff_header {text-align:right}
            .diff_next {background-color:#c0c0c0}
            .diff_add {background-color:#aaffaa}
            .diff_chg {background-color:#ffff77}
            .diff_sub {background-color:#ffaaaa}
            
            * {font-size: small};
        </style>
    </head>
    <body>''')
    
    for diff in file_diffs_perenv:
        for line in diff:
            sys.stdout.write(line)
            
        sys.stdout.write("<br /><br />")
            
    sys.stdout.write("</body></html>")

if __name__ == '__main__':
    
    stdin_targetables = sys.stdin.readlines()
    
    read_targetables(stdin_targetables)
    
    readcontentof_targetables()
    
    organize_targetable_content()
    
    outputdiff_ashtml()
    
    
    

    
    
    
    