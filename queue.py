class Queue:
    def __init__(self):
        self.queue_list = []
    
    def push(self, data):
        self.queue_list.append(data)
    
    def pop(self):
        print(self.queue_list)
        self.queue_list[0] = None