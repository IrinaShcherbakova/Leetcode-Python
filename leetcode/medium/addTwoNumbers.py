# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_length = self.length(l1)
        l2_length = self.length(l2)
        short = (l1 if l1_length < l2_length else l2)
        long = (l1 if l1_length >= l2_length else l2)
        head = long
        carry = 0
        isTail = False
        while short:
            curSum = short.val + long.val + carry
            long.val = curSum % 10
            carry = (1 if curSum >= 10 else 0)
            short = short.next
            if not long.next:
                isTail = True
                break
            long = long.next
        if carry:
            if isTail:
                long.next = ListNode(0)
                long = long.next
            self.addCarry(long)
        return head
            
                 
    def length(self, l: ListNode) -> int:
        count = 0
        while l:
            count += 1
            l = l.next
        return count
    
    
    def addCarry(self, l: ListNode) -> None:
        print("append carry to %s" %l.val)
        carry = 1
        while carry:
            curSum = l.val + carry
            l.val = curSum % 10
            carry = (1 if curSum >= 10 else 0)
            if carry and not l.next:
                l.next = ListNode(0)
            l = l.next         
        return
            
        
        
        
                
