from ex23_solve import *
from ex20_solve import *
from ex17_reimplement import *
class URLRouter():
    def __init__(self, DS):
        self.DS = DS()

    def get_best(self, key):
        #get the best match for what searched
        tem_keyy = None
        value = None
        for i in range(0, len(key)+1):
            tem_key = key[:i]
            if tem_key[len(tem_key)-1:] == '/':
                _value = self.DS.get(tem_key)
                if _value != None:
                    value = _value
                    tem_keyy = tem_key
        if tem_keyy:
            return tem_keyy, value
        else:
            return None

    def get_shortest(self, key):
        match = self.get_all(key)
        if not match: return None
        shortest_k, shortest = match[0]
        for items in match:
            if len(items[0]) < len(shortest_k):
                shortest_k, shortest = items
        return shortest_k, shortest

    def get_longest(self, key):
        match = self.get_all(key)
        if not match: return None
        longest_k, longest = match[0]
        for items in match:
            if len(items[0]) > len(longest_k):
                longest_k, longest = items
        return longest_k, longest

    def add(self, key, value):
        pass

    def get(self, key):
        pass

    def get_all(self, start):
        pass


class TSTRouter(URLRouter):
    def __init__(self):
        super().__init__(TSTree)

    def get(self, key):
        return self.DS.get(key)

    def get_all(self, key):
        results = []
        get = self.DS.find_all(key)
        for item in get:
            results.append((item.key, item.value))
        return results

    def add(self, key, value):
        self.DS.set(key, value)

class BSTRouter(URLRouter):
    def __init__(self):
        super().__init__(BSTree)
    
    def add(self, key, value) :
        self.DS.set(key, value)

    def get(self, key):
        return self.DS.get(key)

    def get_all(self, key):
        results = self._get_all(key, self.DS.root, [])
        return results
    
    def _get_all(self, key, node, results):
        if node.key.startswith(key):
            results.append((node.key, node.value))
        if node.left:
            self._get_all(key, node.left, results)
        if node.right:
            self._get_all(key, node.right, results)
        return results

class DRouter(URLRouter):
    def __init__(self):
        super().__init__(Dictionary)

    def add(self, key, value):
        self.DS.set(key, value)

    def get(self, key):
        return self.DS.get(key)

    def get_all(self, key):
        bucket = self.DS.map.begin
        results = []
        while bucket:
            node = bucket.value.begin
            while node:
                if node.value[0].startswith(key):
                    results.append(node.value)
                node = node.next
            bucket = bucket.next
        return results
