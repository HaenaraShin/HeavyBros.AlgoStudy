/**
* 002. 벌집
* 작성자 : HaenaraShin
* 날 짜 : 2018.02.16
* 언 어 : JAVA
* https://www.acmicpc.net/problem/2292
* 6각형의 벌집의 특정 지점부터 중심까지의 거리
*/

import java.util.*;
import java.math.*; // Math.ceil 과 Math.sqrt 를 사용하기 위해 import

public class Main {
		public static void main(String[] args) {
			Scanner scanner = new Scanner(System.in);
			int input = scanner.nextInt();

			/**
			 * 사실 중간에 어떤경로는 고려할 필요 없이
			 * '중심으로 부터의 거리'만 찾으면 되는데
			 * 각 Depth의 값중 가장 큰 값을 보면 규칙을 쉽게 찾을 수 있다
			 * 1, 7, 19, 37, 61, ...
			 * 이걸 공식으로 풀어보면
			 * Depth 1 => 1
			 * Depth 2 => 1 + (6 * 1)
			 * Depth 3 => 1 + (6 * 1) + (6 * 2)
			 * Depth 3 => 1 + (6 * 1) + (6 * 2) + (6 * 3)
			 * ...
			 * 따라서 Depth가 n 일때 가능한 숫자의 최대값은
			 * Depth n => 1 + 6 * (0부터 n-1까지의 합)
			 * Depth n => 1 + 6 * (n * (n-1) / 2)
			 * 그러므로 예제입력이 x일 때 출력값 y를 방정식으로 정리하면
			 * x = (y * (y-1) /2) * 6 + 1
			 * (x - 1) / 6 = y * (y-1) / 2
			 * (x - 1) / 6 * 2 = y^2 - y
			 * (x - 1) / 6 * 2 + 1/4 = y^2 - y + 1/4 = (y - 1/2)^2
			 * sqrt( (x-1)/6*2 + 1/4 )= y-1/2
			 * sqrt( (x-1)/6*2 + 1/4 ) + 1/2 = y
			 * 여기서 주의할 점은 최대값(1,7,19, ...)일 경우 정수로 딱 떨어질 테지만
			 * 최대값이 아닌경우에는 딱 떨어지지 않고 소수점이 남는데
			 * 소수점이하가 남만큼 '한발짝' 더 가야한다는 의미이므로
			 * 소수점이하 올림(Math.ceil)을 해야 한다.
			 * 따라서 이 것을 C언어로 표현하자면
			 * ceil(sqrt((x - 1) / 6 * 2 + 0.25) + 0.5)
			 */
			double x = (double)input;
			int y = (int) Math.ceil(Math.sqrt((x - 1) / 6 * 2 + 0.25) + 0.5);
			System.out.println(String.format("%d", y));
		}

}

/**
 * 결과
 * 7801684	hamster12345	2292	맞았습니다!!	10948 KB	116 MS	Java / 수정	1732 B	1분 전
 */

 /**
 * 피드백
 *
 */
