# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        x=[]
        a=""
        def dfs(root,a):
            if not root:
                return
            if root.left==None and root.right==None:
                x.append(int(a+str(root.val)))
                return 
            
            dfs(root.left,a+str(root.val))
            dfs(root.right,a+str(root.val))
            
        dfs(root,a)
        
        # print(x)
        return sum(x)
            
            
        