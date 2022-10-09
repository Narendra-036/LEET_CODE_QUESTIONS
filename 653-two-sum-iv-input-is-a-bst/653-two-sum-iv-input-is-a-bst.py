# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp=root
        arr=[]
        def bfs(root,ans):
            if not root:
                return 0
            ans.append(root.val)
            bfs(root.left,ans)
            bfs(root.right,ans)
        bfs(temp,arr)
        for i in range(len(arr)):
            x=k-arr[i] 
            if x in arr:
                for j in range(len(arr)):
                    if x==arr[j] and j!=i:
                        return True
        return False