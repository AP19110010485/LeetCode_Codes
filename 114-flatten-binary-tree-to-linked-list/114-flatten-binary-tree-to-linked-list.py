# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # flatten the left tree, flatten the right tree and attach left tree b/w root and right tree 
        # flatten the root tree and return the tail
        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # Case 1: [No Action ] root.left is empty, then we do not need to attach it on the root's right 
            # Case 2: [No Action] root.left & root.rigth is empty, then we do not need to do anything

            # Case 3: root.left is non-empty, assign root.right to root.left & lefttail.right to root.right

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            # for tail, value should be righttail, if it is empty, then lefttail, and if that is empty then root

            last = rightTail or leftTail or root
            
            return last
        
        return dfs(root)