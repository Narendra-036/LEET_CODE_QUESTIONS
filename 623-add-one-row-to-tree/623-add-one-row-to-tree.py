# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        temp=root
        def hii(temp,d):
            
            if d==2 and temp:
                x=TreeNode(v)
                y=TreeNode(v)
                x.left=temp.left
                y.right=temp.right
                temp.left=x
                temp.right=y
                return root
            else:
                if temp:
                    hii(temp.left,d-1)
                    hii(temp.right,d-1)
            return root
        
        if d==1:
            x=TreeNode(v)
            x.left=root
            return x
        
        return hii(temp,d)