# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        if len(ans)%2==0:
            l=len(ans)//2
            x=ans[l:]
            x=x[::-1]
            
            if ans[:l]==x:
                return True
        else:
            l=len(ans)//2
            x=ans[l+1:]
            x=x[::-1]
            if ans[:l]==x:
                return True
        return False