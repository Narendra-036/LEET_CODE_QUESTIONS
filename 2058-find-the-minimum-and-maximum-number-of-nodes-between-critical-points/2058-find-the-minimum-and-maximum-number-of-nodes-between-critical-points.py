# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head.next
        if not temp or not head:
            return [-1,-1]
        arr=[]
        prev=head
        c=1
        while temp.next:
            c+=1
            if prev.val>temp.val and temp.val<temp.next.val:
                arr.append(c)
            if prev.val<temp.val and temp.val>temp.next.val:
                arr.append(c)
            prev=temp
            temp=temp.next
        if len(arr)<2:
            return [-1,-1]
        arr.sort()
        ma=arr[-1]-arr[0]
        mi=9999999
        for i in range(len(arr)-1):
            mi=min(mi,arr[i+1]-arr[i])
        return [mi,ma]
            
            
            
        