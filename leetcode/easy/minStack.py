class LinkedList:
    def __init_(self):
        self.val = None
        self.min = None
        self.next = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tail = None

    def push(self, x: int) -> None:
        newNode = LinkedList()
        newNode.val = x
        newNode.next = self.tail
        if newNode.next is not None and newNode.next.min < x:
            newNode.min = newNode.next.min
        else:
            newNode.min = x
        self.tail = newNode

    def pop(self) -> None:
        self.tail = self.tail.next

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        return self.tail.min



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push([])
obj.push(-2)
obj.push(0)
#obj.pop()
# param_3 = obj.top()
# print(param_3)
param_4 = obj.getMin()
print(param_4)