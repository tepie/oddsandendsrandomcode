#!/usr/bin/python

import os, sys, re, os.path
import distutils.file_util

EXT_SPLITTER = re.compile("\.")
UNKNOWN_ARTIST = re.compile(re.escape("Unknown Artist/Unknown Album"))

#def form_directory_path(): pass

def move_not_so_best_files(root,not_the_best,dirs):
	#pass
	if not os.path.exists(dirs):
		os.makedirs(dirs)
		
	for name in not_the_best:
		#print root, "|", name ,"|", move_dups_to 
		#print os.path.join(root,name), "|",os.path.join(dirs,name)
		src = os.path.join(root,name)
		dst = os.path.join(dirs,name)
		
		if os.path.exists(src) and os.path.exists(dst):
			distutils.file_util.copy_file(src,dst)
			os.remove(src)
		else:
			if not os.path.exists(src):
				sys.stderr.write("source doesn't exist: %s\n" % src)
			
			if not os.path.exists(dst):
				sys.stderr.write("destination doesn't exist: %s\n" % dst)
		
def determine_best_file(root,similars):
	largest_index = -1
	largest_size = 0
	for possible_index in range(len(similars)):
		possible = similars[possible_index]
		fullpath = os.path.join(root,possible)
		if os.path.exists(fullpath):
			statinfo = os.stat(fullpath)
			if statinfo.st_size > largest_size:
				largest_size = statinfo.st_size
				largest_index = possible_index
		else:
			sys.stderr.write("path doesn't exist: %s\n" % fullpath)
	return possible_index

def examine_files(root, files,dirs):
	
	for name in files:
		name_and_ext = EXT_SPLITTER.split(name)
		
		if len(name_and_ext) == 2:
			base_name = name_and_ext[0]
			base_ext = name_and_ext[1]
			regex = re.compile(re.escape(base_name))
			
			similars = [name]
			for name_again in files: 
				again_name_and_ext = EXT_SPLITTER.split(name_again)
				
				again_base_name = again_name_and_ext[0]
				again_ext = again_name_and_ext[1]
				
				if not name == name_again:
					if not regex.match(again_base_name) == None and base_ext == again_ext: 
						#print name, ",", name_again
						similars.append(name_again)
					
			if len(similars) > 1:
				best_file_index = determine_best_file(root,similars)	
				
				if best_file_index != -1:
					best_file_name = similars.pop(best_file_index)
					#print best_file_index, "|", len(similars), "|",best_file_name , "|", name
					move_not_so_best_files(root,similars,dirs)
				else:
					pass #sys.stderr.write("no best file: %s\n" % root)
			else:
				pass #sys.stderr.write("nothing similar in: %s\n" % root)
				
			
if __name__ == '__main__':
	
	top = sys.argv[1] 
	move_dups_to = sys.argv[2]
	
	for root, dirs, files in os.walk(top, topdown=False): 
		append_directory_tail = re.sub(re.escape(top),"", root)
		to_directory_full = "%s%s" % (move_dups_to,append_directory_tail)
		#print to_directory_full
		
		if UNKNOWN_ARTIST.search(root) == None:
			examine_files(root,files,to_directory_full)
		else:
			sys.stderr.write("skipping directory: %s\n" % root)
			