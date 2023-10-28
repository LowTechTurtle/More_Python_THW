class TSTreeNode():
    def __init__(self, char, key, value, low, eq, high):
        self.char = char
        self.key = key
        self.value = value
        self.low = low
        self.eq = eq
        self.high = high

    def repr(self):
        return f"{self.key}:{self.value}<{self.low and self.low.key}={self.eq and self.eq.key}={self.high and self.high.key}>"
    
class TSTree():
    def __init__(self):
        self.root = None

    def set(self, key, value):
        chars = [ord(x) for x in key]
        self.root = self._set(self.root, chars, key, value)

    def _set(self, node, chars, key, value):
        next_char = chars[0]
        if not node:
            node = TSTreeNode(next_char, None, None, None, None, None)
        if next_char < node.char:
            node.low = self._set(node.low, chars, key, value)
        elif next_char == node.char:
            if len(chars) > 1:
                node.eq = self._set(node.eq, chars[1:], key, value)
            else:
                node.value = value
                node.key = key
        else:
            node.high = self._set(node.high, chars, key, value)
        return node

    def get(self, key):
        chars = [ord(x) for x in key]
        node = self._get(self.root, chars)
        return node and node.value or None

    def _get(self, node, chars):
        char = chars[0]
        if node == None:
            return None
        if char < node.char:
            return self._get(node.low, chars)
        elif char == node.char:
            if len(chars) > 1:
                return self._get(node.eq, chars[1:])
            else:
                return node
        else:
            return self._get(node.high, chars)
     
    def find_all(self, key):
        results = []
        chars = [ord(x) for x in key]
        start = self._get(self.root, chars)
        if start:
            self._find_all(start.eq, key, results)
        return results

    def _find_all(self, node, key, results):
        if not node: return
        if node.key and node.value:
            results.append(node)
        if node.low:
            self._find_all(node.low, key, results)
        if node.eq:
            self._find_all(node.eq, key, results)
        if node.high:
            self._find_all(node.high, key, results)

    def find_part(self, key):
        found = self.find_shortest(key[1:])
        if not found: return None
        for i in range(0, len(key)):
            stem = key[:i]
            node = self.find_shortest(stem)
            if not node:
                return found
            else:
                found = node
        return found

    def find_shortest(self, key):
        nodes = self.find_all(key)
        if nodes:
            shortest = nodes[0]
            for node in nodes:
                if len(node.key) < len(shortest.key):
                    shortest = node
            return shortest
        else:
            return None

    def find_longest(self, key):
        nodes = self.find_all(key)
        longest = nodes[0]
        for node in nodes:
            if len(node.key) > len(longest.key):
                longest = node
        return longest
