class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.count = 0
        self.topElement = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.count += 1
        self.topElement = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        extraQueue = []
        while len(self.queue) > 1:
            extraQueue.append(self.queue.pop(0))
        poppedEl = self.queue.pop(0)
        if len(extraQueue) >= 1:
            while len(extraQueue) > 1:
                self.queue.append(extraQueue.pop(0))
            self.topElement = extraQueue.pop(0)
            self.queue.append(self.topElement)
        else:
            self.topElement = None
        self.count -= 1
        return poppedEl

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topElement

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.count == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
