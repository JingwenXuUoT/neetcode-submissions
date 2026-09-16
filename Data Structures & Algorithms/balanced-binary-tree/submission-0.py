# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right:
            return False
        
        leftH = self.height(root.left)
        rightH = self.height(root.right)

        return abs(leftH-rightH)<=1
    def height(self, root):
        if not root:
            return 0
        
        leftH = self.height(root.left)
        rightH = self.height(root.right)

        return max(leftH, rightH) + 1
        