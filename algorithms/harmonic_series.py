#!/usr/bin/env python
#coding=utf-8

def harmonic(n):
    sum = 0.0
    for i in range(1, n):
        sum += 1.0 / i
    return sum



def main():
    l = [5, 10, 200, 300, 30000, 100000000]
    for n in l:
        print 'n: %s, h(n): %s' % (n, harmonic(n))


main()





'''
n: 5, h(n): 2.08333333333
n: 10, h(n): 2.82896825397
n: 200, h(n): 5.87303094812
n: 300, h(n): 6.27933054697
n: 30000, h(n): 10.8861516588
n: 100000000, h(n): 18.9978964039
'''