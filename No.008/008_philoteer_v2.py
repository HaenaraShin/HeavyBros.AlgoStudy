#!/usr/bin/env python2

import sys

#one shape
def shape(x, y):
	f =  (x**2)*(15/2.0) - (x*33/2.0) + 13
	return not(not(int(f) & 1<<y))

#recursively copy and paste shapes to form the pattern.
def recursive_stamp(n, out, pos):
	if pos == n:
		return out
	else:
		for i in range (0, pos):
			out[i+pos][n-pos-pos:n] = out[i][n-pos:n+pos]
			out[i+pos][n:n+pos] = out[i][n-pos:n+pos]
			 
		pos = 2*pos
		return recursive_stamp(n, out, pos)
	
#main() {

#get input
n = input()
out = []
#init output array
for i in range (0, n):
	out.append([' ']*(2*n-1))

#fill first 3 lines of the array
for i in range (0,3):
	for j in range (0,5):
		out[i][(n - 3)+j] = chr(32 + (shape(i+1,j)*10))

out = recursive_stamp(n, out, 3)

#display
for i in range (0, n):
	print ''.join(out[i][0:2*n-1])
