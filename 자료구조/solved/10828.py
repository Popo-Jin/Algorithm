# https://www.acmicpc.net/problem/10828 : 스택
# 0.5 초 (추가 시간 없음)	256 MB
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import time


start_time = time.time() #시작 시간

import sys

N = int(sys.stdin.readline())
stack = []
index = 0
for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "push":
        stack.append(command[1])
        index += 1
    elif command[0] == "pop":
        if index == 0:
            print(-1)
        else:
            print(stack[index-1])
            stack.pop()
            index -= 1
    elif command[0] == "size":
        print(index)
    elif command[0] == "empty":
        if index == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if index == 0:
            print(-1)
        else:
            print(stack[index-1])

    print("stack : ", stack, "index : ", index)



end_time = time.time() #종료 시간

print("알고리즘 수행 시간 : ", end_time - start_time)
