"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        temp=head
        if not temp:
            return temp
        arr=[]
        while temp:
            if temp.random==None:
                arr.append([temp.val,-1,temp])
            else:
                arr.append([temp.val,temp.random,temp])
            temp=temp.next
        
        rand=[]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][1]==arr[j][2]:
                    rand.append(j)
            if len(rand)!=i+1:
                rand.append(-1)
        # print(rand)
            
        
        nodes=[]
        for i in range(len(arr)):
            nodes.append(Node(arr[i][0]))
        for i in range(len(nodes)):
            if i+1<len(arr):
                nodes[i].next=nodes[i+1]
            if rand[i]==-1:
                nodes[i].random=None
            else:
                
                nodes[i].random=nodes[rand[i]]
        return nodes[0]
        