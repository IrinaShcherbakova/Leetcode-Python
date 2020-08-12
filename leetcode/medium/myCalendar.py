class LinkedList:
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None
    
#     def set_start_time(self, new_time: int) -> None:
#         self.start = new_time

#     def set_end_time(self, new_time: int) -> None:
#         self.end = new_time

class MyCalendar:

    def __init__(self):
        self.head = None
        self.tail = None
    

    def book(self, start: int, end: int) -> bool:
        
        if not self.head:
            self.head = self.tail = LinkedList(start, end)
            return True
        
        # locate the spot where we can place the event
        # s.t. prev.end <= start and next.start >= end
        cur = self.head
        while cur and cur.end <= start:
            cur = cur.next
        
        if cur and self.is_overlap(start, end, cur):
            return False
        
        if cur and cur.prev and self.is_overlap(start, end, cur.prev):
            return False
         
        # append to the list
        event = LinkedList(start, end)
        
        if not cur:
            # append to the tail
            self.tail.next = event
            event.prev = self.tail
            self.tail = event
            return True
        
        #append to the head
        if not cur.prev:
            event.next = cur
            cur.prev = event
            self.head = event
            return True
        
        event.next = cur
        event.prev = cur.prev
        cur.prev.next = event
        cur.prev = event
        
        return True   
        
    def is_overlap(self, start: int, end: int, node: LinkedList) -> bool:
        return start < node.end and node.start < end
    
    
    
    
    
    
    
    
    
    
    
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
