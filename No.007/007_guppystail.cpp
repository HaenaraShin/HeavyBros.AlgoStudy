#include <stdio.h>

int main()
{
	int _size;
	unsigned int _x;
	unsigned int _y;
	unsigned int _distance;
	unsigned int _n;
	scanf("%d", &_size);

	for (int i = 0; i < _size; i++) {
		scanf("%d %d", &_x, &_y);
		_n = 0;
		_distance = _y - _x;

		while (_n *_n < _distance)
			_n++;

		if(_n*_n - _n >= _distance)
			printf("%d\n", 2 * _n - 2);
		else
			printf("%d\n", 2 * _n - 1);
	}

	return 0;
}
//7402479	guppystail	1011	Fly me to the Alpha Centauri	맞았습니다!!	1112 KB	0 MS	C++14	424 B