# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        x=[root]
        k=0
        while x:
            temp=[]
            for i in x:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            k+=1
                
            if k%2==1:
                for i in range(len(temp)//2):
                    temp[i].val,temp[-i-1].val=temp[-i-1].val,temp[i].val
                    
#                 for i in temp:
#                     print(i.val)
            x=temp[::]
        return root
                
                    
            
        