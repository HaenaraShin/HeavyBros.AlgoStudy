import java.util.Scanner;
import java.util.Stack;

public class study {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		Stack<Integer> stack = new Stack<Integer>();

		for(int i = 0; i<n; i++) {
			String str = sc.nextLine();
			String split[] = str.split(" ");
			
			switch(split[0]) {
			
			case "push":
				stack.push(Integer.parseInt(split[1]));
				break;
			
			case "pop":
					if(stack.isEmpty()) {
						System.out.println("-1");
					}
					else {
						System.out.println(stack.pop());
					}
				break;
			
			case "size":
				System.out.println(stack.size());
				break;
			
			case "empty":
				if(stack.isEmpty()) {
					System.out.println("1");
				}else {
					System.out.println("0");
				}
				break;
			
			case "top":
				if(stack.isEmpty()) {
					System.out.println("-1");
				}else {
					System.out.println(stack.peek());
				}
				break;
			
			
			}
			
			
		}
		
	}

}

/*
자료구조로 구현하지 않고 클래스를 호출하여 사용하는 소스
E pop() 메서드 : 스택의 맨 위에서 객체를 제거하고 그 객체를 반환한다.
E push(E item) : 스택의 맨 위에 객체를 추가한다.
E peek() : 스택의 맨 위에 있는 객체를 반환한다. 이 때 객체를 스택에서 제거하지는 않는다.
Boolean empty() : 현재 스택이 비어있는지를 확인한다.
*/





