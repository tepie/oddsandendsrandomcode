#!/usr/bin/python

import sys,re
from bisect import bisect_left

#http://code.google.com/codejam/contest/dashboard?c=351101
#http://stackoverflow.com/questions/212358/binary-search-in-python/2233940#2233940

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end


if __name__ == '__main__':
    
    f = open(sys.argv[1], 'rb')
    lines = f.readlines()
    f.close()
    
    re_no_newline = re.compile("\n$")
    
    cases = int(lines[0])
    
    #print "cases %s" % cases
    
    for case in range(cases):
        credit = lines[(case * 3) + 1]
        items = lines[(case * 3) + 2]
        prices = lines[(case * 3) + 3]
        prices = re_no_newline.sub("",prices)
        
        #sys.stdout.write("credit: %s items: %s prices: %s case: %s\n" % (re_no_newline.sub("",credit),re_no_newline.sub("",items),prices,case))
        #print
        #print re_no_newline.sub("",credit)
        #print prices
        
        price_list = prices.split(" ")
        #price_list.sort()
        
        for price_idx in range(len(price_list)):
            price_value = price_list[price_idx]
            look_for = int(credit) - int(price_value)
            #try: look_for_result = binary_search(price_list,str(look_for))
            try: look_for_result = price_list.index(str(look_for))
            except ValueError: look_for_result = -1
            if (not look_for_result == -1) and (not look_for_result ==  price_idx):
                sys.stdout.write("Case #%s:\t" % (case + 1))
                if price_idx < look_for_result:
                    sys.stdout.write("%s\t%s\n" % (price_idx + 1,look_for_result + 1))
                else:
                    sys.stdout.write("%s\t%s\n" % (look_for_result + 1,price_idx + 1))
                break        
