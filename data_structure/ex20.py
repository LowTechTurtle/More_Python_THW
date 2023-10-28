class BSTreeNode():
    def __init__(self, key, value, parent = None, left = None, right = None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.hash = hash(key)

    def __repr__(self):
        Left = self.left and self.left.key or None
        Right = self.right and self.right.key or None
        Parent = self.parent and self.parent.key or None
        return f'Key: {self.key}, Value: {self.value}, Left: {Left}, Right: {Right}, Parent: {Parent}'

class BSTree():
    def __init__(self, key, value, parent = None, left = None, right = None):
        self.root = BSTreeNode(key, value, parent, left, right)

    def get_node(self, key):
        node = self.root
        while node.key != key:
            if hash(key) >= node.hash:
                if node.right == None:
                    return node, None
                else:
                    node = node.right
            else:
                if node.left == None:
                    return node, None
                else:
                    node = node.left
        return node.parent, node
    def get(self, key):
       par_node, node = self.get_node(key) 
       if node:
           return node.value
       else:
           return None

    def set(self, key, value):
        par_node, node = self.get_node(key)
        if node:
            node.value = value
        else:
            if hash(key) >= par_node.hash:
                par_node.right = BSTreeNode(key, value, parent = par_node)
            else:
                par_node.left = BSTreeNode(key, value, parent = par_node)
    def successor(self, node):
        succ = node.right.hash
        node1 = node.right
        succ_node = node1
        while node1:
            if node1.hash < succ:
                succ = node1.hash
                succ_node = node1
            node1 = node1.right
        node.key = succ_node.key
        node.value = succ_node.value
        return succ_node
    def delete_node(self, node):
        par_node = node.parent
        if node == None:
            return None
        elif node.right == None and node.left == None:
            if par_node.right == node:
                par_node.right = None
                node.parent = None
            else:
                par_node.left = None
                node.parent = None
        elif node.right == None and node.left != None:
            if par_node.left == node:
                par_node.left = node.left
                node.left.parent = par_node
                node.left = None
                node.parent = None
            else:
                par_node.right = node.left
                node.left.parent = par_node
                node.left = None
                node.parent = None
        elif node.right != None and node.left == None:
            if par_node.left == node:
                par_node.left = node.right
                node.right.parent = par_node
                node.right = None
                node.parent = None
            else:
                par_node.right = node.right
                node.right.parent = par_node
                node.right = None
                node.parent = None
        else:
            succ_node = self.successor(node)
            self.delete_node(succ_node)

    def delete(self, key):
        par_node, node = self.get_node(key)
        if node == self.root:
            print("Cannot delete the root of the BSTree")
            return None
        self.delete_node(node)

    def list(self, node):
        print(node)
        if node.left:
            node_left = node.left
            self.list(node_left)
        if node.right:
            node_right = node.right
            self.list(node_right)
