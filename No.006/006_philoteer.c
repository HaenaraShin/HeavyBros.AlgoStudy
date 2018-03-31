#include <stdio.h>
#include <stdlib.h>

int N;
char buf[70];
int cnt = 0;

//
void pseudostack(int val){
	sad_dijkstra:
	
	if (!N)	exit(0);
	
	scanf("%s",buf);
	N--;	
	
	switch (buf[0])
	{
		case 'p':
			if (buf[1] == 'u'){	
				cnt++;
				int val;
				scanf("%d",&val);
				pseudostack(val);
				goto sad_dijkstra;
			}
			else{
				if(cnt)	cnt--;
				printf("%d\n",val);
			}
			break;
		case 's':	
				printf("%d\n",cnt);
				goto sad_dijkstra;
			break;
		case 'e':
				printf("%d\n",(!cnt));
				goto sad_dijkstra;
			break;
		case 't':	
				printf("%d\n",val);
				goto sad_dijkstra;
			break;
	}
	
	if(N && val == -1) goto sad_dijkstra;
}

int main(){
	scanf("%d", &N);
	pseudostack(-1);
	return 0xc0ffee;
}
