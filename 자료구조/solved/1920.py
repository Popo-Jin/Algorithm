# https://www.acmicpc.net/problem/1920
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.



import sys

N = int(sys.stdin.readline())
A = list(map(str,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(str,sys.stdin.readline().split()))
A.sort()
# print(A)
# print(B)
def binary_search(target, data):
    start = 0
    end = len(data)-1
    # print("end : ", end)
    while start <= end:
        # print("start:",start,"end:",end)
        mid = (start+end)//2 
        #// -> 나누기 후 소숫점 자리 버림
        # print("mid : ", mid)
        # print("data[mid]", data[mid])
        if data[mid] == target:
            # print("check")
            return mid
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1

for i in range(len(B)):
    C = binary_search(B[i], A)
    # print("C:",C)
    if C is not None:
        print(1)
    else:
        print(0)
