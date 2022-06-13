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


        