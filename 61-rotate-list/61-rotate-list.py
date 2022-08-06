# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head==None or head.next==None:
            return head
        if head.next.next==None:
            if k%2==0:
                return head
            else:
                x=head
                y=head.next
                x.next=None
                y.next=x
                head=y
                return head
        
        a=head
        count=0
        while a:
            count+=1
            a=a.next
        k=k%count
        
        while k>0:
            x=head
            temp=head
            while x.next.next:
                x=x.next
            y=x.next
            x.next=None
            y.next=temp
            head=y
            k-=1
        return head   
        