# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return None
        q = [root]
        res = []
        while q:
            res.append([])
            children = []
            for i in q:
                if i.left: children.append(i.left)
                if i.right: children.append(i.right)
                res[-1].append(i.val)
            q = children
        return res
        