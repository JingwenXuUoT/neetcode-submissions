# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if not root:
            return []
        
        layer_queue = deque()
        layer_queue.append(root)
        # use [] list, to implement a queue is very inefficient since pop() have to shift all remaining elements over by one
        res = []
        
        while layer_queue:
            size = len(layer_queue)
            for i in range(size):
                node = layer_queue.popleft()
                if i == size-1:
                    res.append(node.val)
                if node.left:
                    layer_queue.append(node.left)
                if node.right:
                    layer_queue.append(node.right)
        
        return res
        