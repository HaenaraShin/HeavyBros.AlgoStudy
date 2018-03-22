import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		System.out.println("숫자를 입력하세요");
		int n = sc.nextInt();	// 입력값
		int a = n/5;			// 필요한 5kg 봉투의 개수
		int answer = 0;			// 정답
		while (true) {
			int da = n-(5*a);	 
			int b = da/3;		// 필요한 3kg 봉투의 개수
			int db = da%3;		
			answer = a+b;		
				if(a<0) {
					System.out.println("-1");
					break;
				} else if(db==0){
//					System.out.println("5kg 봉투 개수 : " + a);
//					System.out.println("3kg 봉투 개수 : " + b);
//					System.out.println("정답은 : " + answer);
					System.out.println(answer);
					break;
				} else {
					a--;
				}
		}
	}
}
