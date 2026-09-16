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
        def dfs(path_max, node):
            if not node:
                return 0
            
            if node.val >= path_max:
                res = 1
            else:
                res = 0
            
            path_max = max(path_max, node.val)
            res += dfs(path_max, node.left)
            res += dfs(path_max, node.right)

            return res
        
        return dfs(root.val, root)
