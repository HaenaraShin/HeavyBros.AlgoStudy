#include <iostream>
#include <memory.h>

using namespace std;

struct position
{
	int ID;
	int Distance;
	char dir;
};
struct	position _info[100000];
struct	position Temp[100000];
int	 IdList[100000];

void MergeSort(struct position arr[], int p, int q)
{
	int mid = 0;
	if (p == q)
		return;
	mid = (p + q) / 2;

	MergeSort(arr, p, mid);
	MergeSort(arr, mid + 1, q);

	{
		struct	position * p1 = &arr[p];
		struct	position * p2 = &arr[mid + 1];
		//Merge
		for (int i = 0; i < q - p + 1; i++)
		{
			int id;
			int val;
			char dir;
			if (p1 != &arr[mid + 1] && (p2 > &arr[q] || p1->Distance < p2->Distance || (p1->Distance == p2->Distance && p1->ID < p2->ID)))
			{
				id = p1->ID;
				val = p1->Distance;
				dir = p1->dir;
				p1++;
			}
			else
			{
				id = p2->ID;
				val = p2->Distance;
				dir = p2->dir;
				p2++;
			}
			Temp[p + i].ID = id;
			Temp[p + i].Distance = val;
			Temp[p + i].dir = dir;
		}
		//Copy
		memcpy(&arr[p], &Temp[p], sizeof(struct position) * (q - p + 1));
	}
	return;
}
int main()
{
	int _T,_N,_L,_k,_id,_dis;
	cin.tie(NULL);
	cin.sync_with_stdio(false);

	cin >> _T;

	for (int i = 0; i < _T; i++) {
		int idIdx = 0;
		cin >> _N >> _L >> _k;
		for (int j = 0; j < _N; j++) {
			cin >> _dis >> _id;
			_info[j].ID = _id;
			IdList[j] = _id;
			_info[j].Distance = _id < 0 ?_dis :  _L - _dis;
			if (_id < 0)
				_info[j].dir = 1;
			else
				_info[j].dir = 0;
		}
		//asign
 		for (int j = 0; j < _N; j++) {
			if (_info[j].dir == 1)
				_info[j].ID = IdList[idIdx++];
		}
		for (int j = 0; j < _N; j++) {
			if (_info[j].dir == 0)
				_info[j].ID = IdList[idIdx++];
		}
		//Sort
		MergeSort(_info, 0, _N - 1);
		cout << _info[_k-1].ID << "\n";
		//Result
	}
	return 0;
}


///163562	guppystail	3163	맞았습니다!!	4720 KB	316 MS	C++14 / 수정	1802 B