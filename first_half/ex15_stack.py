class StackNode():
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f'[{self.value}:{repr(nval)}]'

class Stack():
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            node = StackNode(obj, None)
            self.top = node
        elif self.top != None:
            node = StackNode(obj, self.top)
            self.top = node
            

    def pop(self):
        if self.top == None:
            return None
        else:
            node = self.top
            self.top = self.top.next
            return node.value

    def topp(self):
        if self.top != None:
            return self.top.value
        else:
            return None

    def count(self):
        node = self.top
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
