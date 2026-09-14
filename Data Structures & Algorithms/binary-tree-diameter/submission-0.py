# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # The diameter of a binary tree is the max among the sums of the left height and the right hight of the nodes int he tree
        # DFS, calculate the height of the tree; at each node, the subtrees return their respective heights
        # maitain a global variable to update the maximum diameter as needed during O(n) traversal
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            diameter = max(diameter, leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1
        dfs(root)
        return diameter
        

        