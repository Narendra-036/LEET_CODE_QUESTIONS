# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list2
        while temp.next:
            temp=temp.next
        count=0
        start=list1
        end=list1
        temp1=list1
        while temp1:
            count+=1
            if count==a:
                start=temp1
            if count==b+1:
                end=temp1
            temp1=temp1.next
        
        start.next=list2
        temp.next=end.next
        return list1