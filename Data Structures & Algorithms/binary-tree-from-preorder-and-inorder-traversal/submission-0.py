# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:key for key,val in enumerate(inorder)}
        self.pre_idx = 0
        # pre_idx walks preorder left to right exactly once, in the order nodes are created: root, then left subtree, then right subtree. 

        def constructDFS(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            split = inorder_index[root_val]
            root.left = constructDFS(left, split-1)
            root.right = constructDFS(split+1, right)

            return root
            
        return constructDFS(0, len(inorder)-1)
        