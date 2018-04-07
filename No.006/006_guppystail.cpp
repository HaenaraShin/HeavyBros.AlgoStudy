#include <iostream>

using namespace std;

int _stack[10000];
int _pointer;

void push(int _input)
{
	_stack[_pointer++] = _input;
}

int pop()
{
	if (_pointer == 0)
		return -1;
	else
		return _stack[--_pointer];
}
int size()
{
	return _pointer;
}
int empty()
{
	return _pointer == 0 ? 1 : 0;
}
int top()
{
	if (_pointer == 0)
		return -1;
	else
		return _stack[_pointer-1];
}

int main()
{
	char _command[16];
	int _val;
	int _size;
	cin.tie(NULL);
	cin.sync_with_stdio(false);
	cin >> _size;
	_pointer = 0;
	for (int i = 0; i < _size; i++)
	{
		cin >> _command;
		//parsing command
		if (_command[0] == 'p'
			&& _command[1] == 'u') {
			cin >> _val;
			push(_val);
		}
		else if (_command[0] == 'p'
			&& _command[1] == 'o') {
			cout << pop() << "\n";
		}
		else if (_command[0] == 's') {
			cout << size() << "\n";
		}
		else if (_command[0] == 'e') {
			cout << empty() << "\n";
		}
		else if (_command[0] == 't') {
			cout << top() << "\n";
		}
	}
	return 0;
}

//8300143	guppystail	10828	맞았습니다!!	2028 KB	0 MS	C++14 / 수정	1036 B