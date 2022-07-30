# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        ans=0
        temp=head.next
            
        while temp:
            if temp.val!=0:
                ans+=temp.val
            else:
                arr.append(ans)
                ans=0
            temp=temp.next
            
        dummy=ListNode(0)
        cur=dummy
        for i in arr:
            new=ListNode(i)
            cur.next=new
            cur=new
        return dummy.next
            