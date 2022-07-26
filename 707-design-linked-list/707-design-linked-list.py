class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


class MyLinkedList:

    def __init__(self):
        self.head=ListNode(0)
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for i in range(index+1):
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index<0: 
            index=0
        prep=self.head 
        for i in range(index):
            prep=prep.next
        new_node=ListNode(val)
        new_node.next=prep.next
        prep.next=new_node
        self.size+=1
     
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return 
        prep=self.head 
        for i in range(index):
            prep=prep.next
        prep.next=prep.next.next
        self.size-=1