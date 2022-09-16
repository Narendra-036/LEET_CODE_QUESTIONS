# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        x=[]
        i=0
        j=k
        while i<len(arr) and i+k<=len(arr):
            y=arr[i:j]
            y=y[::-1]
            x+=y
            i+=k
            j+=k
        x+=arr[len(x):]
        node=ListNode(0)
        temp=node
        for i in x:
            i=ListNode(i)
            temp.next=i
            temp=temp.next
        return node.next