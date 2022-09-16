# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        x=[]
        while temp:
            if temp in x:
                return True
            x.append(temp)
            temp=temp.next
        return False
            