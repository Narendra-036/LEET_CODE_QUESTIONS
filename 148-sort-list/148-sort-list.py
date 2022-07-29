# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        for val in arr:
            new=ListNode(val)
            cur.next=new
            cur=cur.next
        return dummy.next
            