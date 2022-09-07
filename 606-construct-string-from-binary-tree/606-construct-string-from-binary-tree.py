# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dsf(root):
            if(root==None):
                return ""
            left="("+ dsf(root.left)    +")"
            right="("+ dsf(root.right)  +")"
            if(left=="()" and right=="()"):
                return str(root.val)
            elif(left and right=="()"):
                return str(root.val)+left
            else:
                return str(root.val)+left+right
        
        return dsf(root)