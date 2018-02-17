/**
* 001. 별찍기1
* 작성자 : HaenaraShin 
* 날 짜 : 2018.02.14
* 언 어 : C
* https://www.acmicpc.net/status/?from_mine=1&problem_id=2438
* 입력받은 숫자만큼 별을 찍는 문제
* 어떤식으로 입력받고 어떤식으로 출력하면 되는지 파악하기 위해 선정
*/

// stdio.h를 import 할 필요는 없다.

int main(){
    int input;
    scanf("%d", &input);               // 입력은 scanf 로 받을 수 있다.
    for(int i = 0; i < input; i++){
        for(int j = 0; j < i+1; j++){
            printf("*");               // 출력은 printf로 할 수 있다.
        }
        printf("\n");                  // 서로에게 피드백은 주석으로
    }
}

/**
* 결과
* 7792244	hamster12345	2438	맞았습니다!!	1116 KB	0 MS	C / 수정	199 B
*/
