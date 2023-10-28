from ex17.ex14 import *
class Dictionary():
    def __init__(self):
        self.map = DLL()
        for i in range(0, 256):
            self.map.push(DLL())

    def hash_key(self, key):
        return hash(key) % 255

    def get_slot(self, key):
        bucket_num = self.hash_key(key)
        bucket = self.map.get(bucket_num)
        if bucket:
            node = bucket.begin
            while node:
                if node.value[0] == key:
                    return bucket, node
                node = node.next
        return bucket, None

    def set(self, key, value):
        bucket, node = self.get_slot(key)
        if node:
            node.value = (key, value)
        else:
            bucket.push((key, value))

    def get(self, key):
        bucket = self.map.get(self.hash_key(key))
        node = bucket.begin
        while node:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        return None

    def delete(self, key):
        bucket = self.map.get(self.hash_key(key))
        node = bucket.begin
        while node:
            if node.value[0] == key:
                bucket.detach_node(node)
            node = node.next

    def list(self):
        bucket_node = self.map.begin
        while bucket_node:
            node = bucket_node.value.begin
            while node:
                print(node.value)
                node = node.next
            bucket_node = bucket_node.next














