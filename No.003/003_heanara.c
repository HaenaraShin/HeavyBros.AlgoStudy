/**
* 003. 분수찾기
* 작성자 : HaenaraShin 
* 날 짜 : 2018.02.17
* 언 어 : C
* https://www.acmicpc.net/problem/1193
* 분수의 규칙을 찾는 문제
* 사실 분수랑은 아무련 관련이 없다..
*/
int main() {
	int input;
	scanf("%d", &input);
	int i = 1; // 분자
	int j = 1; // 분모 
	int sw = 1; // 분자와 분모의 방향을 결정하는 switch
	for (int count = 1; count < input; count++) { // 초기값이 이미 1/1이므로 1부터 시작
		i -= sw;
		j += sw;
		if (j == 0) {
			j = 1;
			sw *= -1; // 분모와 분자의 진행방향을 바꾼다. 
		}
		else if (i == 0) {
			i = 1;
			sw *= -1; // 분모와 분자의 진행방향을 바꾼다. 
		}
	}
	printf("%d/%d\n", i, j);
}
/**
 * 결과
 * 7807034	hamster12345	1193	맞았습니다!!	1116 KB	0 MS	C / 수정	295 B	4분 전
 */