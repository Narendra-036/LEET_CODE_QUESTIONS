# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        x=[]
        for i in lists:
            head=i
            while head:
                x.append(head.val)
                head=head.next
        x.sort()
        dummy=ListNode(0)
        cur=dummy
        for i in x:
            new=ListNode(i)
            cur.next=new
            cur=new
        return dummy.next