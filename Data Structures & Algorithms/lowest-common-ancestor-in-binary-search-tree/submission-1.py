# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root:
        #     return None
        # if root is p:
        #     return p
        # elif root is q:
        #     return q
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if not left and not right:
        #     return None
        # elif left and not right:
        #     return left
        # elif not left and right:
        #     return right
        # else:
        #     return root
        
        # return # this is unreachable, sonce every sub-branch returns

# the above is an accepted version, general for every tree, but not what the interviewer needed.

        # since this is a BST, traversal of this tree should be conditional depends on the value of root, p and q, meaning a (all over) search algorithm is not needed
        cur = root
        while cur:
            if p.val < cur.val and q.val<cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val >cur.val:
                cur = cur.right
            else:
                return cur

