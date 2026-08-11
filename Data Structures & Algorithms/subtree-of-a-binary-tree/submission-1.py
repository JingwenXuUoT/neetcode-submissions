# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Some edge cases
        # then if root.left and if root.right is not needed
        # line 20,21 also not needed
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        # left_bool = False
        # right_bool = False
        # these two should be defined outside the if conditional blocks
        # if root.left:
        left_bool = self.isSubtree(root.left, subRoot)
        # if root.right:
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