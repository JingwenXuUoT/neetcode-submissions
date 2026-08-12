# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breadth First Search
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            cur_level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)
        
        return res
                