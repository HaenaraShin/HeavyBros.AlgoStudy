#!/usr/bin/env python2

import numpy as np

x = int(input("input a number : "))

ar = np.ones([x+1,x+1])
ar_L = np.tril(ar)
ar_affine = (ar_L)*(1 << 5 ^3) + 7
diag_nl = np.identity(x+1) * (ord('@')>>1)
out = (ar_affine - diag_nl).ravel().astype(np.int8)
out = out[1:]
print "".join([chr(i) for i in out])
