class LinkedList:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key].value
            self.remove(key)
            self.add(key, res)  #move node to the beginning of the list
            return res
        return -1
          

    # most recently item is at the beginning of the list
    # least recently item is at the end
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        
        if self.size == self.capacity:
            #remove LRU node
            self.remove(self.tail.key)
        
        self.add(key, value)
        return None
        
 
    # removes node from the linked list
    def remove(self, key: int) -> None:
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.cache.pop(key)
        self.size -= 1
        
        if self.head == node:
            self.head = node.next
            if self.head:
                self.head.prev = None
            if self.tail == node:
                self.tail = self.head
            return None
        
        if self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            return None
        
        node.prev.next = node.next
        node.next.prev = node.prev
        return None
      
        
    # adds new node to the beginning of linked list
    def add(self, key: int, value: int) -> None:
        node = LinkedList(key, value)
        self.cache[key] = node
        self.size += 1
        if not self.head:
            self.head = node
            self.tail = node
            return None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
