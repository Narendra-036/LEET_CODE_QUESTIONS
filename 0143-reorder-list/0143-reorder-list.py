# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp=head
        a=[]
        while temp:
            a.append(temp)
            temp=temp.next
        i=len(a)-1
        temp=head
        for j in range(1,(len(a)//2)+1):
            temp.next=a[i]
            i-=1
            temp=temp.next
            temp.next=a[j]
            temp=temp.next
        temp.next=None
        # for i in range(10):
        #     print(head.val)
        #     head=head.next
            
            