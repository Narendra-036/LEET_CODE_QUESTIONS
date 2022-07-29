# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        if count==1 or head is None:
            head=None
            return head
        x=ListNode(0)
        x.next=head
        head=x
        count=count-n
        temp=head
        while(count>0):
            temp=temp.next
            count-=1
        temp.next=temp.next.next
        
        head=head.next
        return head