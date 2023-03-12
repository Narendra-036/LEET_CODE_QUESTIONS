"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        x=[root]
        while x:
            temp=[]
            for i in x:
                if i.left :
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            for i in range(1,len(temp)):
                temp[i-1].next=temp[i]
            x=temp
        return root
            
                
        