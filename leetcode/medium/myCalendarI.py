class LinkedList:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = None


class MyCalendar:

    def __init__(self):
        self.head = None
        
        
    def book(self, start: int, end: int) -> bool:
        # print("new booking, start: %s, end: %s" % (start,end))
        # self.print_calendar()
           
        if not self.head:
            self.head = LinkedList(start, end)
            return True
        
        prev = None
        cur = self.head
        
        while cur and cur.end <= start:
            prev = cur
            cur = cur.next
            
        if prev and self.is_overlap(prev.start, prev.end, start, end):
            return False
        
        if cur and self.is_overlap(cur.start, cur.end, start, end):
            return False
        
        if cur and cur.next and self.is_overlap(cur.next.start, cur.next.end, start, end):
            return False
        
        booking = LinkedList(start, end)
        if not cur:
            prev.next = booking        
        elif cur == self.head:
            self.head = booking
            booking.next = cur
        else:
            booking.next = cur
            prev.next = booking
        
        return True

    
    def print_calendar(self):
        cur = self.head
        print("*************")
        while cur:
           print("node start: %s, end: %s" % (cur.start, cur.end))
           cur = cur.next
        print("*************")
        
        
    def is_overlap(self, start1, end1, start2, end2):    
        if start1 >= start2 and start1 < end2:
            print("overlap with start1 %s and start2 %s" %(start1, start2))
            return True
        if start2 >= start1 and start2 < end1:
            print("overlap with start1 %s and start2 %s" %(start1, start2))
            return True
        if end1 > start2 and end1 <= end2:
            print("overlap with start1 %s and start2 %s" %(start1, start2))
            return True
        if end2 > start1 and end2 <= end1:
            print("overlap with start1 %s and start2 %s" %(start1, start2))
            return True
        if start1 == start2 and end1 == end2:
            return False
        return False
        
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
