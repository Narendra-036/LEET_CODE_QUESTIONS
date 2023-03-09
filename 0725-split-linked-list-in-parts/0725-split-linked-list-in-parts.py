# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp)
            temp=temp.next
        ans=[]
        l=len(arr)
        x,y = l//k , l%k
        nex=0
        prev=0
        for i in range(k):
            if y:
                nex+=1
                y-=1
            if len(arr)>prev:
                ans.append(arr[prev])
                nex+=x
                arr[nex-1].next=None
                prev=nex
            else:
                ans.append(None)
        return ans
        
        
                