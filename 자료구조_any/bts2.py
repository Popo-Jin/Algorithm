class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data < node.data:
                node.left = self.insert_value(node.left, data)
            elif data > node.data:
                node.right = self.insert_value(node.right, data)
            else:
                return "duplicate data"
        return node

    def find(self, data):        
        return self.find_value(self.root, data)     
    
    def find_value(self, root, data):        
        if root is None or root.data == data:            
            return root is not None       
        elif data < root.data:            
            return self.find_value(root.left, data)        
        else:            
            return self.find_value(root.right, data)

    def delete(self, data):
        self.root, deleted = self.delete_value(self.root, data)
        return deleted
    
    def delete_value(self, node, data):
        if node is None:
            return node, False
        
        deleted = False
        if data == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif data < node.data:
            node.left, deleted = self.delete_value(node.left, data)
        else:
            node.right, deleted = self.delete_value(node.right, data)
        return node, deleted

a = BinarySearchTree()
a.insert(5)
a.insert(4)
a.insert(3)
a.insert(2)
print(a.find(4))
a.delete(4)
print(a.find(4))

