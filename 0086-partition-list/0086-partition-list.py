# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        z=ListNode(0)
        e=z
        y=ListNode(0)
        s=y
        temp=head
        while temp:
            if temp.val>=x:
                n=ListNode(temp.val)
                z.next=n
                z=z.next
            else:
                n=ListNode(temp.val)
                y.next=n
                y=y.next
            temp=temp.next
        y.next=e.next
        return s.next