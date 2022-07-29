# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=""
        b=""
        temp=l1
        while temp:
            a+=str(temp.val)
            temp=temp.next
        temp=l2
        while temp:
            b+=str(temp.val)
            temp=temp.next
        a=str(int(a)+int(b))
        dummy=ListNode(0)
        cur=dummy
        for i in a:
            new=ListNode(int(i))
            cur.next=new
            cur=new
        return dummy.next
            
        