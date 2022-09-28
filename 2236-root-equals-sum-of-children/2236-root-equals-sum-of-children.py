# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, head: Optional[TreeNode]) -> bool:
        x=head.val
        y=head.left.val
        z=head.right.val
        if y+z==x:
            return True
        return False