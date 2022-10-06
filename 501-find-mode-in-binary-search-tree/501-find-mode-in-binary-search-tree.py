# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        
        def help(root,d):
            if not root:
                return 0
            if root.val not in d:
                d[root.val]=1
            else:
                d[root.val]+=1
            help(root.left,d)
            help(root.right,d)
        help(root,d)
        ans=[]
        a=0
        for i in dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True)):
            a=max(d[i],a)
            if d[i]==a:
                ans.append(i)

        return ans