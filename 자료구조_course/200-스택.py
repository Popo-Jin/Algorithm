'''
시간초과로 인해 input() -> sys.stdin.readline()
'''
import sys

class Stack():
    def __init__(self):
        self.Arr = []

    def push(self, data):
        self.Arr.append(data)

    def pop(self):
        if len(self.Arr) == 0:
            print(-1)
        else:
            print(self.Arr.pop())
        

    def size(self):
        print(len(self.Arr))

    def empty(self):
        if len(self.Arr) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.Arr) == 0:
            print(-1)
        else:
            size = self.Arr[len(self.Arr)-1]
            print(size)
a = Stack()
# num = int(input())
num = int(sys.stdin.readline())
for _ in range(num):
    # com = input()
    com = list(map(str, sys.stdin.readline().split()))
    if 'push' in com:
        # com1, com2 = com.split()
        if com[0] == 'push':
            a.push(com[1])
    else:
        if com[0] == 'pop':
            a.pop()
        elif com[0] == 'size':
            a.size()
        elif com[0] == 'empty':
            a.empty()
        elif com[0] == 'top':
            a.top()