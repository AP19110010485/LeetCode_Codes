# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res , q = [] , [root]
        while q:
            res.append(sum([i.val for i in q if i])/len(q))
            q = [child for node in q for child in [node.left,node.right] if child]
        return res
        