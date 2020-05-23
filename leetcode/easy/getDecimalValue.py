# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = []
        while head is not None:
            number.append(head.val)
            head = head.next
        total = 0
        position = 0
        for i in range(len(number)-1, -1, -1):
            total = total + (number[i] * (2**position))
            position += 1
        return total
        
