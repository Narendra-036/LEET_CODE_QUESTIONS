# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        x=[]
        while temp:
            x.append(temp.val)
            temp=temp.next
        j=-1
        ans=0
        for i in range(len(x)//2):
            ans=max(ans,x[i]+x[j])
            j-=1
        return ans