# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        
        left_bool = False
        right_bool = False
        if root.left:
            left_bool = self.isSubtree(root.left, subRoot)
        if root.right:
            right_bool = self.isSubtree(root.right, subRoot)

        if left_bool or right_bool:
            return True

        return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        
        if p.val != q.val:
            return False

        left_bool = self.isSameTree(p.left, q.left)
        right_bool = self.isSameTree(p.right, q.right)

        if not left_bool or not right_bool:
            return False
        
        return True