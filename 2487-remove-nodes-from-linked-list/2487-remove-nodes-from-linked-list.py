# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        temp=head
        while temp:
            x.append(temp.val)
            temp=temp.next
        i=len(x)-1        
        while i>=1:
            
            if x[i]<=x[i-1]:
                
                i-=1
            else:
                
                x.pop(i-1)
                i-=1
                
        dummy=ListNode(0)
        temp=dummy
        for i in x:
            j=ListNode(i)
            temp.next=j
            temp=temp.next
        return dummy.next