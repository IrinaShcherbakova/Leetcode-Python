class Node:
    
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        index_node = None
        if index > self.size // 2:  #node is located closer to the tail
            index_node = self.traverse_backward(self.size-index-1)
        else:
            index_node = self.traverse_forward(index)
        return index_node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node
        self.size += 1
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index == self.size:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        
        
        index_node = None
        if index > self.size // 2:  #node is located closer to the tail
            index_node = self.traverse_backward(self.size-index-1)
        else:
            index_node = self.traverse_forward(index)
        
        node = Node(val)
        node.next = index_node
        node.prev = index_node.prev
        index_node.prev.next = node
        index_node.prev = node
        self.size += 1
        return
        
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        index_node = None
        if index > self.size // 2:  #node is located closer to the tail
            index_node = self.traverse_backward(self.size-index-1)
        else:
            index_node = self.traverse_forward(index)
        
        self.size -= 1
        if not index_node.prev and not index_node.next:
            self.tail = self.head = None
            return
        
        if not index_node.prev:
            self.head = self.head.next
            self.head.prev = None
            return
        
        if not index_node.next:
            self.tail = self.tail.prev
            self.tail.next = None
            return
            
        index_node.prev.next = index_node.next
        index_node.next.prev = index_node.prev
        return
        
    
    def traverse_forward(self, index: int) -> Node:
        first = self.head
        count = 0
        while count < index:
            count += 1
            first = first.next
        return first
    
    
    def traverse_backward(self, index: int) -> Node:
        last = self.tail 
        count = 0
        while count < index:
            count += 1
            last = last.prev
        return last
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
