# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return self.encode(root)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        nodes = []
        data = data.split('-')
        for char in data:
            nodes.append(int(char))
        return self.decode(nodes, 0, len(nodes)-1)
    
    
    def encode(self, root: TreeNode) -> str:
        if not root:
            return ""
        res = str(root.val)
        if root.left:
            res = res + '-' + self.encode(root.left)
        if root.right:
            res = res + '-' + self.encode(root.right)
        return res
        
    
    def decode(self, nodes: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        root = TreeNode(nodes[start])
        if start == end:
            return root
        right = end+1
        for i in range(start+1, end+1):
            if nodes[i] >= root.val:
                right = i
                break
        root.left = self.decode(nodes, start + 1, right - 1)
        root.right = self.decode(nodes, right, end)
        return root
                        
                        
                        
                        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
