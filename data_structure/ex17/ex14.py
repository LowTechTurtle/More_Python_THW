class DLLNode():
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt
    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f'[{self.value}, {repr(pval)}, {repr(nval)}]'

class DLL():
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        if self.begin == None:
            node = DLLNode(obj, None, None)
            self.begin = node
            self.end = self.begin
        else:
            node = DLLNode(obj, self.end, None)
            self.end.next = node
            self.end = node

    def pop(self):
        if self.begin == None:
            return None
        elif self.begin == self.end:
            node = self.begin
            self.begin = None
            self.end = None
            return node.value
        elif self.begin != self.end:
            dis_node = self.end
            self.end = self.end.prev
            self.end.next = None
            return dis_node.value
    
    def shift(self, obj):
        if self.begin == None:
            node = DLLNode(obj, None, None)
            self.begin = node
            self.end = self.begin
        else:
            node = DLLNode(obj, None, self.begin)
            self.begin.prev = node
            self.begin = node

    
    def unshift(self):
        if self.begin == None:
            return None
        elif self.begin == self.end:
            node = self.begin
            self.begin = None
            self.end = None
            return node.value
        else:
            node = self.begin
            self.begin = self.begin.next
            self.begin.prev = None
            return node.value

    def detach_node(self, node):
        if self.begin == self.end:
            self.begin = None
            self.end = None
        elif self.begin == node:
            self.begin = node.next
            self.begin.prev = None
        elif self.end == node:
            self.end = node.prev
            self.end.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def remove(self, obj):
        count = 0
        node = self.begin 
        while node.value != obj:
            node = node.next
            count += 1
        self.detach_node(node)
        return count
    
    def last(self):
        return self.end.value

    def first(self):
        return self.begin.value

    def get(self, index):
        count = 0 
        node = self.begin
        while node != None:
            if count == index:
                return node.value
            node = node.next
            count += 1

    def count(self):
        count = 0
        node = self.begin
        while node != None:
            node = node.next
            count += 1
        return count

    def invariants(self):
        count = self.count()
        if count == 0:
            assert self.begin == None
            assert self.end == None
        elif count == 1:
            assert self.begin == self.end
            assert self.begin.prev == None
            assert self.end.next == None
        elif count > 1:
            assert self.begin != self.end
            assert self.begin.prev == None
            assert self.end.next == None
            node = self.begin
            while node.next != self.end:
                node = node.next
                assert node != None
                assert node.prev != None
                assert node.next != None
                assert node.value != None



