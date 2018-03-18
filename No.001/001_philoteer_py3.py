#!/usr/bin/env python3

import _thread
import time

n = int(input("num:"))

def foo(bar):
	time.sleep(bar/10.0)
	print("*"*bar)

for x in range (1, n+1):
	_thread.start_new_thread(foo,(x,))


time.sleep(n/5)
