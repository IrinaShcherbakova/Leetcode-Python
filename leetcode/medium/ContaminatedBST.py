# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = self.recover(root, 0)
    
    def recover(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        root.val = val
        root.left = self.recover(root.left, val*2 + 1)
        root.right = self.recover(root.right, val*2 + 2)
        return root
        
    def find(self, target: int) -> bool:
        return self.findNode(target, self.root)
             
    def findNode(self, target: int, root: TreeNode) -> bool:
        if root is None:
            return False
        if root.val == target:
            return True
        if root.val > target:
            return False
        if not root.left:
            return self.findNode(target, root.right)
        if not root.right:
            return self.findNode(target, root.left)
        left, right, parent = root.left.val, root.right.val, target
        while parent != left and parent != right:
            if parent < left and parent < right:
                return False
            if parent % 2 == 0:
                parent = (parent-2) // 2
            else:
                parent = (parent-1) // 2
        if parent == left:
            return self.findNode(target, root.left)
        return self.findNode(target, root.right)
    

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
