"""
Node -> data, next로 이루어짐
head -> 시작노드
"""
# 할것 -> self.head를 Node가 아닌 link만으로 구현 (안되는듯)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = Node('head')

    def push(self, data, idx=None):
        if self.head.next == None:
            self.head.next = Node(data)
        elif idx != None:
            newNode = Node(data)
            now = self.get_node(idx)
            newNode.next = now.next
            now.next = newNode
        else:
            now = self.head.next
            while now.next:
                now = now.next
            now.next = Node(data)

    def pop(self, idx=None):
        if self.head.next == None:
            return
        elif idx != None:
            pre = self.get_node(idx-1)
            pre.next = pre.next.next
        else:
            now = self.head.next
            while now.next:
                pre = now
                now = now.next
            pre.next = None
    
    def get_node(self, idx):
        if self.head.next == None or idx == 0:
            return self.head
        else:
            now = self.head.next
            cnt = 1
            while now.next:
                if cnt == idx:
                    return now
                now = now.next
                cnt += 1
            return now

    def printall(self):
        now = self.head
        while now.next:
            now = now.next
            print(now.data)

a = Linked()
a.push(3)
a.push(4)
a.push(5)
a.push(6,0)
a.push(9,1)
a.push(2)
a.pop(1)
a.pop(2)
a.pop()
a.pop(3)
a.printall()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linked:
#     def __init__(self, data):
#         self.head = Node(data)

#     def insert(self, data, idx=None):
#         now = self.head
#         newNode = Node(data)
#         cnt = 1
#         if idx == None:
#             while now.next != None:
#                 now = now.next
#             now.next = newNode
#         else:
#             while now.next != None:
#                 now = now.next
#                 if cnt == idx:
#                     newNode.next = now.next  
#                     now.next = newNode
#                     return
#                 else:
#                     cnt += 1
    
#     def printall(self):
#         now = self.head
#         while now != None:
#             print(now.data)
#             now = now.next

#     def delete(self, idx=None):
#         now = self.head
#         cnt = 1
#         if idx == 1:
#             now.next = now.next.next
#         while now.next != None:
#             now = now.next
#             if cnt == idx-1:
#                 now.next = now.next.next
#                 return
#             cnt += 1

# a = Linked(0) #0
# a.insert(3) #0 3
# a.insert(5) #0 3 5
# a.insert(4,1) #0 3 4 5
# a.insert(10,3) #0 3 4 5 10
# # a.delete(3) #0 3 4 10
# # a.delete(3) #0 3 4
# a.insert(12,1)
# a.delete(1)
# a.printall()
