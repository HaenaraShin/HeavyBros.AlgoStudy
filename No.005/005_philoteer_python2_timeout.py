#!/usr/bin/env python2

#I NEED NUMPY
import sys

#test cases
tests = input()

#load an experiment to lists.
#(directly reads stdin)
def sim_init(N,L,k):
	
	ants_leftheading = []
	ants_rightheading = []
	#parse,store
	for x in range (0,N):
		ant = sys.stdin.readline()
		foo,bar = ant.split()
		ant_id = int(bar)
		ant_pos = int(foo)
		ant_direction = (ant_id  >=0)*2-1
		ant_dist = ant_pos if (ant_direction== -1) else L - ant_pos
		
		#poor man's object
		ant = (ant_id, ant_pos, ant_dist)
		
		if ant_direction == -1:
			ants_leftheading.append(ant)
		else:
			ants_rightheading.append(ant)
					
	#sort by distance
	ants_leftheading.sort(key=lambda tup: tup[2])
	ants_rightheading.sort(key=lambda tup: tup[2])
	#return
	return (ants_leftheading,ants_rightheading)

#updates the ant list.
#(occurs during the simulation)
#returns the id of the ant to drop
def update_antlist_right(ant,ants,L):
	#ant =  (ant_id, ant_pos, ant_dist)
	
	#if the right-heading ant at the leftmost position doesn't collide with the falling ant:
	if ants[-1][1] > ant[1]:
		return ant[0]
		
	#if not: 
	return_val = ants[-1][0]

	k = len(ants) -1
	if k == 0:
		ants[0] = (ant[0],ants[0][1],ants[0][2])
		return return_val


	#update the array
	while ants[k][1] < ant[1] and k > 0:
		ants[k] = (ants[k-1][0],ants[k][1],ants[k][2])
		k-=1
	
	ants[k+1] = (ant[0],ants[k+1][1],ants[k+1][2])
	
	return return_val
	
#updates the ant list. (#2)
#(occurs during the simulation)
#returns the id of the ant to drop
def update_antlist_left(ant,ants,L):
	#ant =  (ant_id, ant_pos, ant_dist)
	
	#if the left-heading ant at the rightmost position doesn't collide with the falling ant:
	if ants[-1][1] < ant[1]:
		return ant[0]
		
	#if not:
	return_val = ants[-1][0]
	
	k = len(ants) -1
	if k == 0:
		ants[0] = (ant[0],ants[0][1],ants[0][2])
		return return_val

	#update the array
	while ants[k][1] > ant[1] and k > 0:
		ants[k] = (ants[k-1][0],ants[k][1],ants[k][2])
		k-=1
	
	ants[k+1] = (ant[0],ants[k+1][1],ants[k+1][2])
	
	return return_val

#int main() {
for x in range (0,tests):
	#n,l,k
	nlk = sys.stdin.readline()
	N,L,k = nlk.split()
	N = int(N)
	L = int(L)
	k = int(k)
	ants_leftheading,ants_rightheading = sim_init(N,L,k)

	#sanity check
	if k > N:
		print "k out of bound"
		sys.exit(0)

	#ant_list[i] =  (ant_id, ant_pos, ant_dist)
	#smaller = faster falling

	#the main simulation loop.
	cnt = 0	#counts the mortality rate of the ants.
	t = 0 #time
	drop_log = []	#list of ants dropped (id, time)

	while cnt < k:		

		#if one array is empty: process the non-empty array.
		if len(ants_rightheading) == 0 and len(ants_leftheading) != 0:
			ant = ants_leftheading.pop(0)
			t = ant[2] + 1
			drop_log.append((ant[0],t))
			cnt+=1
			
		elif len(ants_rightheading) != 0 and len(ants_leftheading) == 0:
			ant = ants_rightheading.pop(0)
			t = ant[2] + 1
			drop_log.append((ant[0],t))
			cnt+=1
		
		#two arrays have some elements.
		#ant_left will fall first
		elif ants_leftheading[0][2] < ants_rightheading[0][2]:
			ant = ants_leftheading.pop(0)
			t = ant[2] + 1
			new_id = update_antlist_right(ant,ants_rightheading,L)
			drop_log.append((new_id,t))
			cnt+=1
		
		#ant_right will fall first 
		elif ants_leftheading[0][2] > ants_rightheading[0][2]:
			ant = ants_rightheading.pop(0)
			t = ant[2] + 1
			new_id = update_antlist_left(ant,ants_leftheading,L)
			drop_log.append((new_id,t))
			cnt+=1
			
		#two ants fall together. (smaller falls a bit faster)
		else:
			ant_left = ants_leftheading.pop(0)
			t = ant_left[2] + 1
			new_id_1 = update_antlist_right(ant_left,ants_rightheading,L)

			ant_right = ants_rightheading.pop(0)
			
			if len(ants_leftheading) >0:
				new_id_2 = update_antlist_left(ant_right,ants_leftheading,L)
			else:
				new_id_2 = ant_right[0]
	
			#smaller gos first.
			if new_id_1 < new_id_2:
				drop_log.append((new_id_1,t))
				drop_log.append((new_id_2,t))
			else:
				drop_log.append((new_id_2,t))
				drop_log.append((new_id_1,t))
			cnt+=2
	
	print drop_log[k-1][0]	
	print drop_log
			
#todo: 
#-faster searching (instead of o(n))
#-popping the first element of a list sounds like a poor idea - check how the Python List obj is implemented? (Is is efficient when used as a queue?)
