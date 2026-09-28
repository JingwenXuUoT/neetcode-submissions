# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal on a BST is a sorted ascending order list
        # DFS but maintain a cnt to avoid full traversal
        cnt = k
        res = root.val
        def inOrderDFS(node):
            nonlocal cnt, res
            if not node:
                return
            
            inOrderDFS(node.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            inOrderDFS(node.right)
        
        inOrderDFS(root)

        return res
        # O(h+k), O(h) for the recusion stack

