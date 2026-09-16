# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # backtrack DFS traversal
        # maintain a local max per path, carray this along the path
        # maintian a global count, if max is smaller than current node val, add 1 to res
        res = 0
        def dfs(path_max, node):
            nonlocal res
            if not node:
                return
            
            if node.val >= path_max:
                path_max = node.val
                res += 1
            
            dfs(path_max, node.left)
            dfs(path_max, node.right)

        dfs(root.val, root)
        
        return res
