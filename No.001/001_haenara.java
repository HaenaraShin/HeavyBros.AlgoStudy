/**
* 001. 별찍기1
* 2018.02.16 HaenaraShin
* https://www.acmicpc.net/status/?from_mine=1&problem_id=2438
* 입력받은 숫자만큼 별을 찍는 문제
* 어떤식으로 입력받고 어떤식으로 출력하면 되는지 파악하기 위해 선정
*/

// C와 달리 JAVA는 백준알고리즘에 제출 요령이 까다롭다.
// 1. import java.util.* 를 해야만 Scanner와 print를 사용할 수 있고
// 2. Class 명은 반드시 Main 이어야 하고
// 3. 반드시 public static void main(String[] args) 로 main을 선언해야 한다.

import java.util.*; // Scanner 와 print 를 하기 위해서 '반드시' import

public class Main { // Class 이름이 다르면 컴파일에러가 나므로 무조건 Main

	public static void main(String[] args) {
    // main 함수도 반드시 이렇게 써야만 컴파일 에러가 안난다. 파라미터 까지도!
        Scanner scanner = new Scanner(System.in);
		int input = scanner.nextInt(); // 입력은 Scnner로 받는다.
		for (int i = 0; i < input; i++){
			for (int j = 0; j < i+1; j++){
				System.out.print("*"); // 출력은 System.out.print
			}
			System.out.println(""); // 또는 println 까지 허용
		}
	}
}

/**
 * 결과
 * 7801597	hamster12345	2438	맞았습니다!!	9676 KB	160 MS	Java / 수정	323 B	2분 전
 */

 /**
 * 피드백
 *
 */
