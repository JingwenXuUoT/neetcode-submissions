# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, min_bound, max_bound) -> bool:
            if not node:
                return True

            if not (min_bound < node.val < max_bound):
                return False
            
            return isValid(node.left, min_bound, node.val) and isValid(node.right, node.val, max_bound)

        return isValid(root, float('-inf'), float('inf'))
