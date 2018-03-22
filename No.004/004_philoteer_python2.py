#!/usr/bin/env python2

n=input()
b=n%5
c=n/5-b%3
print -1+(c+b*2%5+1)*(c>-1)
