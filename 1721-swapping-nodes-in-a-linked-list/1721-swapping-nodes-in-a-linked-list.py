# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        end=count-k
        temp=head
        while k-1>0:
            temp=temp.next
            k-=1
        temp1=head
        while end>0:
            temp1=temp1.next
            end-=1
        # print(temp.val)
        # print(temp1.val)
        temp.val,temp1.val=temp1.val,temp.val
        return head