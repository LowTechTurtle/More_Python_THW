class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            # nothing net
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end
        assert self.end.next == None


    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            self.end = node
            return node.next.value
        assert self.end.next == None

    def shift(self, obj):
        if self.begin == None:
           node = SingleLinkedListNode(obj, None)
           self.begin = node
           self.end = self.begin
        elif self.begin:
            node = SingleLinkedListNode(obj, self.begin)
            self.begin = node

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            if node == self.end:
                break
            node = node.next
            
        return count 

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None
        elif self.begin == self.end:
            x = self.begin.value
            self.begin = None
            self.end = None
            return x
        else:
            x = self.begin.value
            self.begin = self.begin.next
            return x

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        assert self.begin != None
        node = self.begin
        count = 0
        if self.begin == None:
            pass
        elif (self.begin == self.end) and (self.begin.value == obj):
            self.begin = None
            self.end = None
            return 0
        elif (self.begin.value == obj) and (self.begin != self.end):
            self.begin = self.begin.next 
            return 0
        while node.next != None:
            count += 1
            prenode = node
            node = node.next
            if node.value == obj:
                prenode.next = node.next
                return count

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def get(self, index):
        """Get the value at index."""
        count = 0
        node = self.begin
        while node != None:
            if count == index:
                return node.value
            if node == self.end:
                break
            node = node.next
            count += 1
