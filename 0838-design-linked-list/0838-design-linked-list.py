class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode()
        
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
        if index > self.size: # We don't have equal to size because equal to size means out of bounds
            return 
        
        if index < 0:
            index = 0
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        node_to_add = ListNode(val)
        node_to_add.next = curr.next
        curr.next = node_to_add
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)