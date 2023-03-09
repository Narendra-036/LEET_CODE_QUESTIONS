# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        x=[]
        while temp:
            if temp in x:
                for i in range(len(x)):
                    if temp==x[i]:
                        return x[i]
            x.append(temp)
            temp=temp.next
        return None