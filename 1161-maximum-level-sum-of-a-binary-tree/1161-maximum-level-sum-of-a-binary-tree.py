# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=[root]
        x=[root.val]
        ans=-999999999999
        s=0
        count=1
        while q:
            # print(sum(x))
            if sum(x)>ans:
                ans=max(ans,sum(x))
                s=count
            x=[]
            for _ in range(len(q)):
                cur=q.pop(0)
                if cur.left:
                    q.append(cur.left)
                    x.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    x.append(cur.right.val)
            count+=1
        return s
                
            