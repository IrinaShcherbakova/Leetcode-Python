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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if head and not root:
            return False
        if head.val == root.val and self.check_path(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    
    def check_path(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        while head.next:
            if root.left and root.right and head.next.val == root.left.val and head.next.val == root.right.val:
                return self.check_path(head.next, root.left) or self.check_path(head.next, root.right)
            if root.left and head.next.val == root.left.val:
                root = root.left
            elif root.right and head.next.val == root.right.val:
                root = root.right
            else:
                return False
            head = head.next
        return (True if not head.next else False)
            
        
    
    
    
    
    
    
    
        
