class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        
        
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            # updates it to most recently used
            self._remove(node)
            self._add(node)
            
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add(newNode)
        else:

            self.cache[key] = Node(key, value)
            node = self.cache[key]
            self._add(node)
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)