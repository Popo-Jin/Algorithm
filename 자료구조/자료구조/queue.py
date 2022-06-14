# 큐를 사용하는 이유
# - 순서대로 처리하기 위해
# CPU 태스크, 은행업무, 프로세스 관리

class Queue:
    def __init__(self):
        self.queue_list = []
    
    def push(self, data):
        self.queue_list.append(data)
    
    def pop(self):
        print(self.queue_list.pop(0))

    def printall(self):
        print(self.queue_list)

a = Queue()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.pop()
a.pop()
a.printall()


        