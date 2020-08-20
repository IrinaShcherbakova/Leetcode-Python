class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.first = self.last = 0
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == len(self.queue):
            return False
        if self.queue[self.last] is not None:
            self.last = (0 if self.last == len(self.queue)-1 else self.last + 1)
        self.queue[self.last] = value    
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.queue[self.first] = None
        if self.first != self.last:
            self.first = (0 if self.first == len(self.queue)-1 else self.first + 1)
        self.size -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size == 0:
            return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size == 0:
            return -1
        return self.queue[self.last]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
