# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        arr=[]
        count=0
        while temp:
            arr.append(temp.val)
            temp=temp.next
        x=[arr[i] for i in range(len(arr)) if i%2==0]
        y=[arr[i] for i in range(len(arr)) if i%2==1]
        arr=x+y
        z=ListNode(0)
        x=z
        for i in arr:
            i=ListNode(i)
            x.next=i
            x=x.next
        return z.next
            
        