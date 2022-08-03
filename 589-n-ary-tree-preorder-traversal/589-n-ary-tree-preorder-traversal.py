"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def func(x):
            if not x:
                return 
            ans.append(x.val)
            for i in x.children:
                func(i)
        func(root)
        return ans
#         order = []
#         def helper(root):
#             if not root: return
#             order.append(root.val)
#             for child in root.children:
#                 helper(child)
                
#         helper(root)
#         return order