# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q=[root]
        ans=[]
        if root ==None:
            return []
        while q:
            mx=-9999999999999999
            for _ in range(len(q)):
                cur=q.pop(0)
                mx=max(mx,cur.val)
                if cur.right: q.append(cur.right)
                if cur.left: q.append(cur.left)
            ans.append(mx)
        return ans
        