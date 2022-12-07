# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        arr=[]
        def search(x:Optional[TreeNode],low,high):
            if not x:
                return 0
            if x.val<=high and x.val>=low:
                
                arr.append(x.val)
            search(x.left,low,high)
            search(x.right,low,high)
        search(root,low,high)
        
        return sum(arr)