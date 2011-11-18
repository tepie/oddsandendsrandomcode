#!/usr/bin/python

import sys,re

if __name__ == '__main__':
    
    f = open(sys.argv[1], 'rb')
    lines = f.readlines()
    f.close()
    
    lines = lines[1:]
    
    re_no_newline = re.compile("\n$")
    re_whitespace = re.compile("\s")
    
    for indx in range(len(lines)):
        line = lines[indx]
        line = re_no_newline.sub("",line)
        words = re_whitespace.split(line)
        
        head = 0
        tail = len(words)
        while head < tail:
            tmp = words[head]
            words[head] = words[tail -1]
            words[tail - 1] = tmp
            head = head + 1
            tail = tail - 1
        
        sys.stdout.write("Case #%s: %s\n" % ( (indx + 1), " ".join(words)))