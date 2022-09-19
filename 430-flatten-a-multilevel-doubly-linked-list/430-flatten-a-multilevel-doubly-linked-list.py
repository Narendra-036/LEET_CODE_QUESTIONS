"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        temp=head
        x=[]
        ans=[]
        while temp:
            ans.append(temp.val)
            if temp.child:
                
                x.append(temp)
                temp=temp.child
            else:
                temp=temp.next
        x=x[::-1]
        for i in x:
            temp=i.next
            while temp:
                ans.append(temp.val)
                temp=temp.next
        
        head=Node(ans[0])
        temp=head
        for i in ans[1:]:
            i=Node(i)
            i.prev=temp
            temp.next=i
            temp=temp.next
        return head
            