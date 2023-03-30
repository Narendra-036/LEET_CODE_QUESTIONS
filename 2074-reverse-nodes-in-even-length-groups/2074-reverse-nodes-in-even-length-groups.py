# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        ans=ListNode(0)
        ans_temp=ans
        x=1
        while temp:
            aux=[]
            for i in range(x):
                if temp:
                    aux.append(temp)
                    temp=temp.next
                else:
                    break
            if len(aux)%2==0:
                for i in aux[::-1]:
                    ans_temp.next=i
                    ans_temp=ans_temp.next
            else:
                for i in aux:
                    ans_temp.next=i
                    ans_temp=ans_temp.next
            x+=1
        ans_temp.next=None
        return ans.next                
                
                    
                
                
        