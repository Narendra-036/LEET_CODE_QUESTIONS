class CustomStack:

    def __init__(self, maxSize: int):
        self.s=maxSize
        self.arr=[]

    def push(self, x: int) -> None:
        if len(self.arr)<self.s:
            self.arr.append(x)
        

    def pop(self) -> int:
        if self.arr:
            c=self.arr[-1]
            self.arr=self.arr[:-1]
            return c
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.arr)<k:
            k=len(self.arr)
            
        for i in range(k):
            self.arr[i]+=val
            pass
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)