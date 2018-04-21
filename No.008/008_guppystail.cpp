#include <stdio.h>

int flag[2000];
int _curflag[2000];

void printTree(int _curLine, int _length)
{
	int totalSmallTree = _curLine / 3 + 1;
	for (int i = 0; i < _length - _curLine - 1; i++)
	{
		printf(" ");
	}
	for (int i = 0; i < totalSmallTree; i++) {
		if ((i == 0 || i == totalSmallTree - 1)
			|| !(flag[i-1] == flag[i])
			|| totalSmallTree == 1) {
			if (_curLine % 3 == 0)
				printf("*");
			else if (_curLine % 3 == 1)
				printf("* *");
			else
				printf("*****");
			_curflag[i] = 1;
		}
		else
		{
			if (_curLine % 3 == 0)
				printf(" ");
			else if (_curLine % 3 == 1)
				printf("   ");
			else
				printf("     ");

			_curflag[i] = 0;
		}
		if (totalSmallTree != 1
			&& i < totalSmallTree - 1) {
			if (_curLine % 3 == 0)
				printf("     ");
			else if (_curLine % 3 == 1)
				printf("   ");
			else
				printf(" ");
		}
	}
	//print remain space...
	for (int i = 0; i < _length - _curLine - 1; i++)
	{
		printf(" ");
	}
	if (_curLine % 3 == 2) {
		for (int i = 0; i < totalSmallTree; i++) {
			flag[i] = _curflag[i];

		}
	}

	printf("\n");
}

int main()
{
	int _size;

	scanf("%d", &_size);
	flag[0] = 1;
	for (int i = 0; i < _size; i++) {
		printTree(i,_size);
	}
	return 0;
}
	guppystail	2448	별찍기 - 11	맞았습니다!!	1128 KB	272 MS	C++14	1272 B