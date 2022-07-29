# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        temp=list1
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        temp=list2
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        for i in arr:
            new=ListNode(i)
            cur.next=new
            cur=cur.next
    
    
        return dummy.next