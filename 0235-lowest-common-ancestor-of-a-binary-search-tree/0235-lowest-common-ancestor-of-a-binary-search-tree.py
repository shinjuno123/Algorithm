# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, large = min(p.val, q.val), max(p.val, q.val)

        # 1 case
        # if root.val < small -> move right
        # if large < root.val -> move left
        # if small <= root.val <= large -> we found LCA

        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
        
         