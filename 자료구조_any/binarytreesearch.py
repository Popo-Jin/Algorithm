class treeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class bts:
    def root(self, data):
        self.root = treeNode(data)
        return self.root

    def insert(self, data):
        now = self.root
        newNode = treeNode(data)
        while now:
            if data < now.data: # 현재 노드보다 작은 경우
                if now.left != None: # 왼쪽 노드가 존재할 경우
                    now = now.left
                else:
                    now.left = newNode
                    return
            elif data > now.data: # 현재 노드보다 큰 경우
                if now.right != None: # 오른쪽 노드가 존재할 경우
                    now = now.right
                else:
                    now.right = newNode
            else: # 현재 노드와 같은 경우 종료
                return
            
    def delete(self, data):
        parent = None
        now = self.root
        while now != None:
            if data == now.data:    # 같으면 종료
                break
            parent = now
            if data < now.data: #왼쪽 자식노드로
                now = now.left
            else:
                now = now.right #오른쪽 자식노드로
        if now == None: #찾을 수 없으면 종료
            return
        if now.left == None and now.right == None:  #자식노드가 없을경우
            if parent != None:  #root가 아닐경우
                if parent.left == now:  #현재노드가 부모의 왼쪽노드일 경우
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.head = None
        elif now.left == None or now.right == None:
            if now.left != None:
                parent.left = now.left
            else:
                parent.right = now.right
        else: #자식노드가 둘다 존재할 경우, 왼쪽 최댓값 또는 오른쪽 최솟값으로 교체
            node_max_left = now.left
            while node_max_left.right != None:
                node_max_left = node_max_left.right
            if parent != None:
                
            elif parent.left == now.left:
                parent.left = node_max_left
            else:
                parent.right = node_max_left

# delete가 좀 어렵네, 지우고 다시
                
            
        
    
    def search(self, node, data):
        if node != None:
            if data < node.data:
                self.search(node.left, data)
            elif data > node.data:
                self.search(node.right, data)
            else:
                return print("Found")
        
    def preorder(self, node):
        if node != None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


a = bts()
root = a.root(9)
a.insert(3)
a.insert(10)
a.insert(2)
a.insert(5)
a.insert(17)
a.delete(9)
# a.search(root, 10)
a.preorder(root)
