class FrontMiddleBackQueue:

    def __init__(self):
        self.arr=[]

    def pushFront(self, val: int) -> None:
        self.arr=[val]+self.arr

    def pushMiddle(self, val: int) -> None:
        x=len(self.arr)//2
        self.arr=self.arr[:x]+[val]+self.arr[x:]

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        ans=0
        if self.arr:
            ans=self.arr[0]
            self.arr=self.arr[1:]
            return ans
        return -1

    def popMiddle(self) -> int:
        ans,x=0,0
        if self.arr:
            x=((len(self.arr)+1)//2)-1
            ans=self.arr[x]
            self.arr=self.arr[:x]+self.arr[x+1:]
            return ans
        return -1

    def popBack(self) -> int:
        ans=0
        if self.arr:
            ans=self.arr[-1]
            self.arr=self.arr[:-1]
            return ans
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()