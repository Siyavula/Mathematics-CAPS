#!/usr/bin/env python

#
#
#  Check a few things in each file and print out some stats
#


import os
import sys





if __name__ == "__main__":
    texfiles = [f for f in os.listdir(os.curdir) if os.path.splitext(f)[1] == '.tex' if f[0]=='G']
    

    print 'Number of occurrences of these things in each file'
    print  '''Filename%s\t{\t}\t(\t)\t[\t]\tbegin\tend''' %(27*' ')
    print '-'*80

    for f in texfiles:
        content = open(f,'r').read()
        matching_items = '{,},(,),[,],\\begin,\\end'
        print f, (35-len(f))*' ',
        for m in matching_items.split(','):
            print '\t',content.count(m),
        print
