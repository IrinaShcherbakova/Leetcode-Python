# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes = self.toArray(head)
        return self.buildSubtree(nodes, 0, len(nodes))
        
    
    def buildSubtree(self, nodes: List[int], start: int, end: int) -> TreeNode:
        if start >= end:
            return None
        mid = start + (end-start)//2
        root = TreeNode(nodes[mid])
        # print("root is %s" %root.val)
        root.left = self.buildSubtree(nodes, start, mid)
        root.right = self.buildSubtree(nodes, mid+1, end)
        return root
        
    
    def toArray(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
        
