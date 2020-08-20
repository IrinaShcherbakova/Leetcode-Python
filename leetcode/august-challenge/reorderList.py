# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        mid, head = self.traverse(head, 1)    
        return head
    
    
    # return len of the list and nodes in the second half    
    def traverse(self, head: ListNode, count: int) -> tuple:
        if not head.next:   # reach the tail
            mid = count//2 + 1
            if count > mid:
                head.next = ListNode(0) # dummy node
            return mid, [head]
        
        mid, nodes = self.traverse(head.next, count + 1)
        
        if count > mid:
            nodes.append(head)
            return mid, nodes
        
        if count == mid: # we hit the future last node of the reordered list
            head.next = None
            return mid, nodes
            
        if count == len(nodes):
            # pop the last node and insert it as head.next
            last = nodes.pop()
            if last.next:
                last.next = head.next
            head.next = last
        return mid, nodes
           
                
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
        
        
        
