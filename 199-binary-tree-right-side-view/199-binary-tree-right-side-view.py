# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root:
            queue = [root]
            while len(queue) > 0:
                view.append(queue[-1].val)
                newQueue = []
                for node in queue:
                    if node.left:
                        newQueue.append(node.left)
                    if node.right:
                        newQueue.append(node.right)
                queue = newQueue
        return view
        