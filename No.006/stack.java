import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Stack stack = new Stack();
    Scanner scanner = new Scanner(System.in);
    int cmdCtr = scanner.nextInt();
    String cmd;
     
    for(int i = 1; i <= cmdCtr; i++) {
      cmd = scanner.next();
      if(cmd.equals("push")){
        int x = scanner.nextInt();
        stack.push(x);
      } else if(cmd.equals("pop")) {
        stack.pop();
      } else if(cmd.equals("size")) {
        stack.size();
      } else if(cmd.equals("empty")) {
        stack.empty();
      } else if(cmd.equals("top")) {
        stack.top();
      }
    }
  }
  static class Stack {
    private int size = 0;
    private SNode top = null;
     
    private class SNode {
      int data;
      private SNode next;
    }
     
    public void top() {
      if (top == null){
        System.out.println(-1);
      } else {
        System.out.println(top.data);
      }
    }
    public void empty() {
      if (size == 0) {
        System.out.println(1);
      } else {
        System.out.println(0);
      }
    }
    public void size() {
      System.out.println(size);
    }
    public void push(int x) {
      SNode node = new SNode();
      node.data = x;
      node.next = top;
      top = node;
      size++;
    }
    public void pop() {
      if (size == 0) {
        System.out.println(-1);
      } else {
        System.out.println(top.data);
        top = top.next;
        size--;
      }
    }
  }
}
/*채점 번호	아이디	문제 번호	결과	메모리	시간	언어	코드 길이	제출한 시간
8408387	whkgudwns	10828	맞았습니다!!	25912 KB	460 MS	Java / 수정	1554 B	*/