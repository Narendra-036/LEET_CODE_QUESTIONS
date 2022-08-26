# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        x=head
        while x:
            a.append(x.val)
            x=x.next
        a.sort()
        dummy=ListNode(0)
        x=dummy
        for i in a:
            j=ListNode(i)
            x.next=j
            x=x.next
        return dummy.next