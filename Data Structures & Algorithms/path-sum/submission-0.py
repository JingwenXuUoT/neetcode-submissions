# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # iterative DFS: simulate it using an explicit stack. Each stack stores a node and the remaning sum needed to reach the target from that node
        #->avoids recursion depth issues for very deep trees
        if not root:
            return False
        
        stack = [(root, targetSum-root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0: # a root to leaf path and sum to target
                return True
            if node.right:
                stack.append((node.right, curr_sum-node.right.val))
            if node.left:
                stack.append((node.left, curr_sum-node.left.val))
        
        return False # stack empty with no valid path
        # O(n), O(n)