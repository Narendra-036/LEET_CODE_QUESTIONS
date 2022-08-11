# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, l, u):
            if not node:
                return True
            if node.val <= l or node.val >= u:
                return False
            return check(node.left, l, node.val) & check(node.right, node.val, u)
        return check(root, -float('inf'), float('inf'))