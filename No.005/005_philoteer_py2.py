#!/usr/bin/env python2

#I NEED NUMPY
import sys

#load an experiment to lists.
#(directly reads stdin)
def sim_init(N,L,k):
	
	ants_leftheading = []
	ants_rightheading = []
	ants_omni = []
	#parse,store
	for x in range (0,N):
		#read stdin
		ant = sys.stdin.readline()
		#split by spaces
		foo,bar = ant.split()
		#id / position / direction / distance to the edge)
		ant_id = int(bar)
		ant_pos = int(foo)
		ant_direction = (ant_id  >=0)
		ant_dist = ant_pos + ant_direction*(L-2*ant_pos)
		
		#store into a tuple.
		ant = (ant_id, ant_pos, ant_dist)
		
		#append to a list
		ants_omni.append(ant)	#stores all ants
		if ant_direction:
			ants_rightheading.append(ant)	#stores right-heading ants
		else:
			ants_leftheading.append(ant)	#stores left-heading ants
					
	#return
	return (ants_omni,ants_leftheading,ants_rightheading)

#find an ant which got dropped.
def ant_find(ant,ant_rightheading,ant_leftheading,ants_omni_srt2):
	#left-heading
	if ant[0] < 0:
		i = ants_leftheading.index(ant)
		ans = ants_omni_srt2[i][0]
	#right-heading
	else:
		i = ants_rightheading.index(ant)
		ans = ants_omni_srt2[-1-i][0]

	return ans

#int main() {
#test cases
tests = input()

for x in range (0,tests):
	#get n,l,k
	nlk = sys.stdin.readline()
	N,L,k = nlk.split()
	N = int(N)
	L = int(L)
	k = int(k)

	#sanity check
	if k > N:
		print "k out of bound"
		sys.exit(0)

	#fill in the data array
	ants_omni,ants_leftheading,ants_rightheading = sim_init(N,L,k)

	#ant_list[i] =  (ant_id, ant_pos, ant_dist)
	#smaller = faster falling

	#sort by distance to the edge
	ants_omni.sort(key=lambda tup: tup[2])
	#sort by position
	ants_omni_srt2 = sorted(ants_omni, key=lambda tup:(tup[1]))
	#sort by distance to the edge (for left/right heading ants)
	ants_leftheading.sort(key=lambda tup: tup[2])
	ants_rightheading.sort(key=lambda tup: tup[2])
				
	#two ants falls at the same time - the one that falls first should be returned..
	if len(ants_omni) > k and ants_omni[k][2] == ants_omni[k-1][2]:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		ant2 = ants_omni[k]	
		ans2 = ant_find(ant2,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print min(ans,ans2)

	#two ants falls at the same time - the one that falls second should be returned..
	elif ants_omni[k-2][2] == ants_omni[k-1][2]:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		ant2 = ants_omni[k-2]	
		ans2 = ant_find(ant2,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print max(ans,ans2)
	#only one ant falls.
	else:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print ans
