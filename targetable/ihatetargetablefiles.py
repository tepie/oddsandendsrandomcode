#!/usr/bin/python

import os,sys,re,difflib

env_groups = {}
file_groups = {}
file_groups_details = {}

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
        
        if not env_groups.has_key(env):
            env_groups[env] = []
            
        if not file_groups.has_key(file_minus):
            file_groups[file_minus] = []
            
        env_groups[env].append(targetable)
        file_groups[file_minus].append(targetable)
        
def lookat_targetables(diff_html=False):
    for k,v in file_groups.iteritems():
        sys.stderr.write("%s, %s\n" % (k,v))
        
        if not file_groups_details.has_key(k):
            file_groups_details[k] = {}
        
        file_groups_details[k]["file_list_length"] = len(v)
        file_groups_details[k]["file_differences"] = []
        
        last_file_content = None
        last_file_name = None   
        
        for file in v:
            f = open(file, 'r')
            content = f.readlines()
            f.close()
            
            file_groups_details[k][file] = content
            
            if not last_file_content == None:
                #for line in difflib.unified_diff(last_file_content, content, fromfile='', tofile=file):
                #    sys.stdout.write(line)  
                if diff_html:
                    diff = difflib.HtmlDiff(wrapcolumn=60).make_file(last_file_content,content,fromdesc=last_file_name, todesc=re.split("/",file)[-1],context=True)
                else:
                    diff = difflib.unified_diff(last_file_content, content, fromfile=last_file_name, tofile=re.split("/",file)[-1])
                file_groups_details[k]["file_differences"].append(diff)
                    
                #sys.stdout.write(diff)
            
            #sys.stdout.write("\n===========\n")
            
            last_file_content = content
            basename = re.split("/",file)[-1]
            last_file_name = basename
            
def outputhtml_targetables():
    sys.stdout.write('''<html><head>
    <style type="text/css">
        table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}
    </style>
</head>
<body>''')
    
    for k in file_groups_details.keys():
        sys.stdout.write("<h1>%s</h1>" % k)
        for diff in file_groups_details[k]["file_differences"]:
            sys.stdout.write(diff)
            
    sys.stdout.write("</body></html>")

if __name__ == '__main__':
    
    stdin_targetables = sys.stdin.readlines()
    
    read_targetables(stdin_targetables)
    
    lookat_targetables(diff_html=True)
    
    outputhtml_targetables()
    
    
    

    
    
    
    