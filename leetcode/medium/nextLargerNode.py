# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        return self.traverse(head, [])
    
    def traverse(self, node: ListNode, stack: List[int]) -> List[int]:
        if node is None:
            return []
        
        if node.next is None: #we reached end of the list
            stack.append(node.val)
            return [0]
        
        res = self.traverse(node.next, stack)
        
        if node.val < stack[-1]:
            res = [stack[-1]] + res
            stack.append(node.val)
            return res
            
        while len(stack) > 0 and node.val >= stack[-1]:
            stack.pop()
        
        if len(stack) > 0:
            res = [stack[-1]] + res
        else:
            res = [0] + res    
        stack.append(node.val)
        return res
            
            
            
            
            
            
        
