# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root):
            if not root: return 0
            sm = dfs(root.left) + (root in [p,q]) + dfs(root.right)
            if sm > 1: self.ans = root
            return min(sm, 1)
        
        dfs(root)
        return self.ans
        