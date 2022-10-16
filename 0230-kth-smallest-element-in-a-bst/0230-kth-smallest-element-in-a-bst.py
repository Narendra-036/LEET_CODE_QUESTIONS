# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        
        def dfs(head,arr):
            if not head:
                return 1
            arr.append(head.val)
            dfs(head.left,arr)
            dfs(head.right,arr)
        
        dfs(root,arr)
        arr.sort()
        return arr[k-1]