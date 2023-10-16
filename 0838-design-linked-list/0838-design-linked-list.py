class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        
        if index > self.size:
            return 
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        node_to_add = ListNode(val, next=curr.next, prev=curr)
        next_node = curr.next
        curr.next = node_to_add
        next_node.prev = node_to_add
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        next_node = curr.next.next
        curr.next = next_node
        next_node.prev = curr
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)