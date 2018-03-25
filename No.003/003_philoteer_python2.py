#!/usr/bin/env python2

import math

def n_sum(n):
	return (n*(n+1))/2

def n_sum_inv(n):
	return int(math.ceil(0.5*(math.sqrt(8*n+1)-1)))

n = input()
dist_norm1 = n_sum_inv(n) + 1

dist_x = dist_norm1 -1 - n_sum(dist_norm1-1) + n 
dist_y = dist_norm1 - dist_x

if (dist_norm1%2):
	dist_x, dist_y = dist_y, dist_x

print str(dist_y) + "/" + str(dist_x)
