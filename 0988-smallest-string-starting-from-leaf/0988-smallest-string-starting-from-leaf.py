# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # print(ord("a")) 97/\
        # print(ord("z")) 122
        ans=[]
        def dfs(root,a):
            if not root.left and not root.right:
                a+=chr(97+root.val)
                ans.append(a[::-1])
                return
            if root.left:
                dfs(root.left,a+chr(97+root.val))
            if root.right:
                dfs(root.right,a+chr(97+root.val))
        
        dfs(root,"")
        print(ans)
        ans.sort()
        return ans[0]
        
        
#         path=[]
#         a=""
#         def dfs(root,a):
#             if not root:
#                 return
#             if root.left==None and root.right==None:
#                 path.append(a+str(root.val))
#                 return 
            
#             dfs(root.left,a+str(root.val)+"+")
#             dfs(root.right,a+str(root.val)+"+")
            
#         dfs(root,a)
#         print(path)
        
#         possible=[]
#         z=999
#         for i in path:
#             x=list(map(int,i.split("+")))
#             possible.append(x)
#             if x[-1]<z:
#                 z=x[-1]
        
#         while True:
            
#             v=[]
#             for i in 
        
        
        
        
        
        
        # ans=""
        # s=99999999999
        # for i in range(len(x)):
        #     j=x[i].replace("+","")
        #     # print(int(j[::-1]))
        #     if int(j[::-1])<s:
        #         ans=x[i]
        #         s=int(j[::-1])
        # ans=list(map(int,ans.split("+")))
        # sol=""
        # for i in ans[::-1]:
        #     sol+=chr(i+97)
        # return sol
            
            
#             k=list(map(int,i[1:].split("+")))
            
#             print(k)
        
        
        
        
#         x={}
#         a=[]
#         def dfs(root,a):
#             print(a)
#             if not root:
#                 return
#             if root.left==None and root.right==None:
                
#                 if sum(a) not  in x:
#                     x[sum(a)]=a
                    
#                 return 
#             a.append(root.val)
#             dfs(root.left,a)
#             dfs(root.right,a)
        
#         dfs(root,a)
#         print(x)