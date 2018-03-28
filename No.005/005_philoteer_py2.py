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
	ants_omni = []
	#parse,store
	for x in range (0,N):
		ant = sys.stdin.readline()
		foo,bar = ant.split()
		ant_id = int(bar)
		ant_pos = int(foo)
		ant_direction = (ant_id  >=0)
		ant_dist = ant_pos + ant_direction*(L-2*ant_pos)
		
		#poor man's object
		ant = (ant_id, ant_pos, ant_dist)
		
		ants_omni.append(ant)
		if ant_direction:
			ants_rightheading.append(ant)
		else:
			ants_leftheading.append(ant)
					
	#return
	return (ants_omni,ants_leftheading,ants_rightheading)

def ant_find(ant,ant_rightheading,ant_leftheading,ants_omni_srt2):
	if ant[0] < 0:#left-heading
		i = ants_leftheading.index(ant)
		ans = ants_omni_srt2[i][0]

	else:
		i = ants_rightheading.index(ant)
		ans = ants_omni_srt2[-1-i][0]

	return ans

#int main() {
for x in range (0,tests):
	#n,l,k
	nlk = sys.stdin.readline()
	N,L,k = nlk.split()
	N = int(N)
	L = int(L)
	k = int(k)

	#sanity check
	if k > N:
		print "k out of bound"
		sys.exit(0)

	ants_omni,ants_leftheading,ants_rightheading = sim_init(N,L,k)

	#ant_list[i] =  (ant_id, ant_pos, ant_dist)
	#smaller = faster falling

	ants_omni.sort(key=lambda tup: tup[2])
	ants_omni_srt2 = sorted(ants_omni, key=lambda tup:(tup[1]))
	ants_leftheading.sort(key=lambda tup: tup[2])
	ants_rightheading.sort(key=lambda tup: tup[2])
				
	if len(ants_omni) > k and ants_omni[k][2] == ants_omni[k-1][2]:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		ant2 = ants_omni[k]	
		ans2 = ant_find(ant2,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print min(ans,ans2)

	elif ants_omni[k-2][2] == ants_omni[k-1][2]:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		ant2 = ants_omni[k-2]	
		ans2 = ant_find(ant2,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print max(ans,ans2)
	else:
		ant = ants_omni[k-1]	
		ans = ant_find(ant,ants_rightheading,ants_leftheading,ants_omni_srt2)
		print ans
