class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent
            self._remove(self.cache[key])
            self._add(self.cache[key])
            
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self._add(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self._add(self.cache[key])
            
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)