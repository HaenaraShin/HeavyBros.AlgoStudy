#include <stdio.h>

int main()
{
	int _input;
	int remain;
	int _3cnt = 0;
	int _5cnt = 0;
	scanf("%d", &_input);
	remain = _input;
	while (remain > 2)
	{
		if (remain % 3 == 2) {
			_5cnt++;
			remain -= 5;
		}
		else if (remain % 3 == 0 && (remain / 3) % 5 == 0) {
			_5cnt += 3;
			remain -= 15;
		}
		else if (remain % 5 == 0) {
			_5cnt++;
			remain -= 5;
		}
		else {
			_3cnt++;
			remain -= 3;
		}
	}
	if (remain != 0)
		printf("-1\n");
	else
		printf("%d\n", _3cnt + _5cnt);

	return 0;
}

7324000	guppystail	2839	맞았습니다!!	1112 KB	0 MS	C++14 / 수정	532 B