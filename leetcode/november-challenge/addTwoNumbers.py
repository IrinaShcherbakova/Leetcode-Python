# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.adjust_len(l1, l2)
        carry = self.add_lists(l1, l2)
        if carry:
            head = ListNode(1, l1)
            return head
        return l1
    
    
    def add_lists(self, l1: ListNode, l2: ListNode) -> int:
        # print("l1: %s, l2: %s" %(l1.val, l2.val))
        if not l1.next:  # we reach tail
            carry = 1 if l1.val + l2.val >= 10 else 0
            l1.val = (l1.val + l2.val) % 10
            return carry
        carry = self.add_lists(l1.next, l2.next)
        # print("old value %s" %l1.val)
        new_carry = 1 if (l1.val + l2.val + carry) >= 10 else 0
        l1.val = (l1.val + l2.val + carry) % 10
        # print("new value %s" %l1.val)
        return new_carry
        
        
    def length(self, l: ListNode) -> int:
        res = 0
        while l:
            res += 1
            l = l.next
        return res
    
    
    def adjust_len(self, l1: ListNode, l2: ListNode) -> tuple:
        len1 = self.length(l1)
        len2 = self.length(l2)
        # print("len1: %s, len2: %s" %(len1, len2))
        if len1 == len2:
            return l1, l2
        smaller = l1 if len1 < len2 else l2
        bigger = l1 if len1 > len2 else l2
        difference = abs(len1 - len2)
        smaller_head = smaller
        while difference:
            zero_node = ListNode(0, smaller_head)
            smaller_head = zero_node
            difference -= 1
        return smaller_head, bigger
            
            
            
            
            
            
            
        
