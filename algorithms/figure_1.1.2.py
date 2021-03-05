#!/usr/bin/env python
#coding=utf-8

# import math

def sqrt(c):
    '''
    calc the sqrt of a number
    '''
    if c < 0:
        print 'Not a number.'
        return
    err = 1e-15
    t = c * 1.0
    while (abs(t - c/t) > err * t):
        t = (c/t + t) / 2.0
    return t;




def main():
    l = [1, 4, 100, 400]

    for c in l:
        print 'c: %s, sqrt: %s' % (c, sqrt(c))

main()




'''
如何理解呢？
t - c/t 趋近于一个几乎为0的数 -> t^2 = c
(c/t + t) / 2.0 当作是两倍的根，但是一直会比两倍的根大。
'''

'''
c: 1, sqrt: 1.0
c: 4, sqrt: 2.0
c: 100, sqrt: 10.0
c: 400, sqrt: 20.0
'''