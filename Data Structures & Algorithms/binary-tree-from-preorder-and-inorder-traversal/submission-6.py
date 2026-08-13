# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:key for key,val in enumerate(inorder)} # this step is important for O(1) lookup
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

        # if len(preorder)==0 or len(inorder)==0:
        #     return None
        
        # root = TreeNode(preorder[0])
        # split = inorder.index(preorder[0]) # scans the list linearly to find the value,O(k)
        # root.left = self.buildTree(preorder[1:split+1], inorder[0:split]) # preorder[1:split+1] copies every element in the range to a new list, so this line not only recurses but opens extra space
        # root.right = self.buildTree(preorder[split+1:], inorder[split+1:])

        # return root
        