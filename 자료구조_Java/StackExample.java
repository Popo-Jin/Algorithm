// 스택은 대표적인 자료구조중 하나로, 가장 마지막에 들어간 데이터가 가장 먼저 나오는 
// 후입선출, LIFO (Last In First Out) 형식의 자료구조다.
// 활용방법으로는
// 웹 브라우저 뒤로가기 : 가장 마지막에 열린 페이지부터 나온다.
// 실행 취소 (undo) : 가장 마지막에 실행된 것부터 실행을 취소한다. (ctrl + z)
// 함수 호출 : 프로그램에서 함수를 호출할 때, 함수가 끝나면 원래 코드로 돌아가야 한다. 이런 함수의
// 정보를 저장하는 메모리를 콜 스택이라고 한다.
// 기능으로는
// push() : 데이터를 넣는 메소드
// pop() : 데이터를 빼는 메소드
// top(), peek() : 데이터를 빼지 않고, 가장 위에 있는 데이터를 확인하는 메소드
// 자세히 설명하면, push는 데이터를 하나씩 담는다.
// pop은 최근에 들어온 데이터를 가져오고, 그 데이터를 지우고, 다시 pop을 하면, 2번째로 나중에
// 들어온 데이터가 나오고 삭제된다.
// top과 peek은 만드는 사람에따라 같은 기능에 다른 이름을 붙인 거다. 기능은 pop과 다르게, 데이터를
// 삭제하지 않고, 최근에 들어온 데이터를 확인하는 것이다.


import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();
        stack.push("1th");
        stack.push("2nd");
        stack.push("3rd");
        System.out.println("stack: "+stack);
        System.out.println(stack.pop());
        System.out.println(stack.peek());
        System.out.println(stack.pop());
        System.out.println("stack: "+stack);
    };
}
