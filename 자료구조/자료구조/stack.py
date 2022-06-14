# 스택을 사용하는 이유
# - 이전 상태를 기억하기 위해
# ex)재귀호출, 브라우저 뒤로가기, undo
class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        self.stack_list.pop()

    def top(self):
        return self.stack_list[len(self.stack_list)-1]

    def printall(self):
        print(self.stack_list)

a = Stack()
a.push(3)
a.push(5)
a.push(1)
a.push(2)
# print(a.top())
a.pop()
print(a.top())
a.printall()
