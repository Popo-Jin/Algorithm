class Node:
    def __init__(self, data):
        self.data = data
        self.rlink = None
        self.llink = None

class deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data) 
            self.head.llink = newNode #head가 가리키던 노드 왼쪽링크를 새 노드로
            newNode.rlink = self.head #새 노드의 오른쪽링크를 head가 가리키던 노드로
            self.head = newNode #head가 가리키는 노드를 새로 insert한 노드로 변경

    def insert_tail(self, data):
        if self.tail == None:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data)
            self.tail.rlink = newNode #tail이 가리키던 노드 오른쪽링크를 새 노드로
            newNode.llink = self.tail #새 노드의 왼쪽 링크를 tail이 가리키던 노드로
            self.tail = newNode #tail이 가리키는 노드를 새로 insert한 노드로 변경

    def delete_head(self):
        if self.head == self.tail: #노드가 1개일 때
            if self.head == None:
                self.head = self.tail = None
            else: #노드가 0개일 때
                return
        else: #노드가 여러개일 때
            self.head = self.head.rlink #head가 가리키는 노드를 오른쪽링크로 옮김
            self.head.llink = None #옮긴 노드의 llink를 None으로 설정

    def delete_tail(self):
        if self.tail == self.head:
            if self.tail == None:
                return
            else:
                self.tail = self.head = None
        else:
            self.tail = self.tail.llink
            self.tail.rlink = None

    def printall(self):
        tmp = self.head #head 포인터값을 옮기면 문제가 생기므로 임시변수에 담음
        while tmp: #head에 값이 있는동안 rlink로 순차적 검색
            print(tmp.data)
            tmp = tmp.rlink

            


a = deque()
a.insert_head(0)
a.insert_head(-1)
a.insert_head(-2)
a.insert_tail(1)
a.insert_tail(2)
# a.printall()
a.delete_head()
a.delete_tail()
# a.printall()
a.delete_tail()
a.delete_tail()
a.printall()
a.delete_tail()
# a.printall()

# print(id(f.head))
# print(id(a.tail))   