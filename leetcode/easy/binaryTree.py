# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Given a binary tree and a sum, determine if the tree
    # has a root - to - leaf path such that adding up all
    # the values along the path equals the given sum.
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.right is None and root.left is None and root.val == sum:
            return True
        currentSum = sum - root.val
        return self.hasPathSum(root.left, currentSum) or self.hasPathSum(root.right, currentSum)

    def isSymmetric(self, root):
        if root is None:
            return False

    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def minDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        minVal = 0
        if root.left is not None:
            minVal = self.minDepth(root.left)
        if root.right is not None:
            if minVal == 0:
                minVal = self.minDepth(root.right)
            else:
                minVal = min(minVal, self.minDepth(root.right))
        return minVal + 1
        




tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)
print("res is %s" % tree.hasPathSum(tree, 21))

