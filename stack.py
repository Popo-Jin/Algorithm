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
