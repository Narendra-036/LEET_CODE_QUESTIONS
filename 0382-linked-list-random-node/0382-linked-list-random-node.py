# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr=[]
        while head:
            self.arr.append(head)
            head=head.next
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr).val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()