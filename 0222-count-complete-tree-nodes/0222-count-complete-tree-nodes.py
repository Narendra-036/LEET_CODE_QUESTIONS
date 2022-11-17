# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def check(root):
            if root:
                self.count+=1
                if root.left:
                    check(root.left)
                if root.right:
                    check(root.right)

        self.count=0
        check(root)
        return self.count