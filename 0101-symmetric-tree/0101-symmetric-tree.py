# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(x,y):
            if x is None and y is None:
                return True 
            if x is None or y is None:
                return False
            
            return (x.val==y.val) and check(x.left,y.right) and check(x.right, y.left)
        if root.left==None and root.right==None:
            return True
        else:
            return check(root.left,root.right)
            