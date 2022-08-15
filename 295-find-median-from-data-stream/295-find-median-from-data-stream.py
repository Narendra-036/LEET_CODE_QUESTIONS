class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)==1:
            return self.arr[0]
        if len(self.arr)%2==0:
            i=len(self.arr)//2
            return (self.arr[i]+self.arr[i-1])/2
        else:
            i=len(self.arr)//2
            return self.arr[i]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()