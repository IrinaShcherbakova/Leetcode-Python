class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.first = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        if self.first is None:
            self.first = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        stack2 = []
        while len(self.stack) > 1:
            stack2.append(self.stack.pop())
        poppedEl = self.stack.pop()
        if len(stack2) >= 1:
            self.first = stack2.pop()
            self.stack.append(self.first)
            while len(stack2) > 0:
                self.stack.append(stack2.pop())
        else:
            self.first = None
        return poppedEl

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.first

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
