

import java.util.Scanner;
public class Main{		//백준 알고리즘에서 Main 클래스를 선언하지 않으면 컴파일 에러 발생
    public static void main(String args[]){
        int a=0, b=0, n=0;
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        a = n/5;
        n%=5;
        while(a>=0){
            if(n%3==0){
                b= n/3;
                n%=3;
                break;
            }
            a--;
            n+=5;
        }
        System.out.printf("%d", n == 0 ? a+b:-1);
    }
}

/*
채점 번호	아이디		문제 번호	문제 제목	결과		메모리	시간	언어	코드 길이	
7944451		whkgudwns	2839		설탕 배달	맞았습니다!!	9868 KB	124 MS	Java	471 B
*/