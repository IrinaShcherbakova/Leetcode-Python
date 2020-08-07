# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        x_nodes = {}
        self.traverse(root, 0, 0, x_nodes)
        res = []
        for key in sorted(x_nodes):
            vert_line = []
            heap = x_nodes[key]
            while heap:
                y, val = heappop(heap)
                vert_line.append(val)
            res.append(vert_line)
        return res
                 
    
    # x, y are coordinates of the root
    def traverse(self, root: TreeNode, x: int, y: int, x_nodes: dict) -> None:
        if not root:
            return
        if x in x_nodes:
            heap = x_nodes[x]
            heapq.heappush(heap, (y, root.val))
        else:
            heap = []
            heapq.heappush(heap, (y, root.val))
            x_nodes[x] = heap
        self.traverse(root.left, x-1, y+1, x_nodes)
        self.traverse(root.right, x+1, y+1, x_nodes)
        return
            
