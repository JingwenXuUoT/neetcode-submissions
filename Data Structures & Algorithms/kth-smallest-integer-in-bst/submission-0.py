# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal on a BST is a sorted ascending order list
        # DFS
        def inOrderDFS(node, res):
            if not node:
                return
            
            if node.left:
                inOrderDFS(node.left, res)
            res.append(node)
            if node.right:
                inOrderDFS(node.right, res)
            
            return
        
        cnt = 1
        res = []
        inOrderDFS(root, res)

        return res[k-1].val

