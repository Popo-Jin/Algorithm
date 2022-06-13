"""
Node -> data, next로 이루어짐
head -> 시작노드
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data, idx=None):
        now = self.head
        newNode = Node(data)
        cnt = 1
        if idx == None:
            while now.next != None:
                now = now.next
            now.next = newNode
        else:
            while now.next != None:
                now = now.next
                if cnt == idx:
                    newNode.next = now.next  
                    now.next = newNode
                    return
                else:
                    cnt += 1
    
    def printall(self):
        now = self.head
        while now != None:
            print(now.data)
            now = now.next

    def delete(self, idx=None):
        now = self.head
        cnt = 1
        if idx == 1:
            now.next = now.next.next
        while now.next != None:
            now = now.next
            if cnt == idx-1:
                now.next = now.next.next
                return
            cnt += 1

a = Linked(0) #0
a.insert(3) #0 3
a.insert(5) #0 3 5
a.insert(4,1) #0 3 4 5
a.insert(10,3) #0 3 4 5 10
# a.delete(3) #0 3 4 10
# a.delete(3) #0 3 4
a.insert(12,1)
a.delete(1)
a.printall()
