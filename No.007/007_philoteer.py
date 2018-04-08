#!/usr/bin/env python2

import math
import sys

def main():
	n = input()
	for i in range (0, n):
		foo = sys.stdin.readline()
		bar,baz = foo.split()
		dist = int(baz) - int(bar)
		print est(dist)

def est(d):
	est_even = int(math.ceil(0.5*(math.sqrt(4*d+1)-1)))*2
	est = est_even -1*((((est_even/2)*(est_even/2+1)) - d) >= (est_even/2.0))
	return est

main()
