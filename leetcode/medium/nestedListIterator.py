# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = []
        self.flatten(nestedList, 0, self.nums)
        self.size = len(self.nums)
        self.index = 0
        
        
    def flatten(self, nestedList: [NestedInteger], index: int, res: List[int]) -> None:
        if index >= len(nestedList):
            return
        
        if nestedList[index].isInteger():
            res.append(nestedList[index].getInteger())
            return self.flatten(nestedList, index+1, res)
        
        # nested list holds a list. Flatten a list first, then recurse with the next index
        inner_list = nestedList[index].getList()
        self.flatten(inner_list, 0, res)
        self.flatten(nestedList, index+1, res)
        return
        
        
    def next(self) -> int:
        val = self.nums[self.index]
        self.index += 1
        return val
        
    
    def hasNext(self) -> bool:
        return self.index < self.size

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
