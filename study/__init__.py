__author__ = 'jinlong'


# for i in xrange(1,10,1):
#     # print 'i',i
#     for y in xrange(1,10,1):
#         print '%s*%s ==%s' % (i,y,i*y)

#! /usr/bin/python
# Filename : table_9x9.py
# Author : Jesse
# Date : 2011/08/13 21:50

print '\n9x9 Table\n'

for i in range(1, 10) :
    for j in range(1, i+1) :
        print j, 'x', i, '=', j*i, '\t',
        # print '%d x %d = %d\t' %(j, i, j*i),
    print '\n'

print '\nDone!'