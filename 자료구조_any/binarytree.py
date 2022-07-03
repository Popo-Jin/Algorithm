class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedTree:
    
    def makeNode(self, left, data, right):
        newNode = Node(data)
        self.data = newNode.data
        newNode.left = left
        newNode.right = right
        return newNode

    def preorder(self, node):
        if node != None:
            print(node.data, end="")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.data, end="")
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end="")
        
a = LinkedTree()
b1 = a.makeNode(None, 'D', None)
b2 = a.makeNode(None, 'C', None)
b3 = a.makeNode(b2, 'A', b1)
a.preorder(b3)
a.inorder(b3)
a.postorder(b3)
