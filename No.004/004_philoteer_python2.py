#!/usr/bin/env python2

n=int(input())
if (n==4) or (n==7):
    print('-1')
else:
    print str(n/5-n%5%3+(n%5<<1)%5)
