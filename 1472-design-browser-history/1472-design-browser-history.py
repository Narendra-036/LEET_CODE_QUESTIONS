class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr=[homepage]
        self.pointer=len(self.arr)-1

    def visit(self, url: str) -> None:
        self.arr=self.arr[:self.pointer+1]+[url]
        self.pointer+=1

    def back(self, steps: int) -> str:
        self.pointer-=steps
        if self.pointer<0:
            self.pointer=0
            return self.arr[self.pointer]
        return self.arr[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer+=steps
        if self.pointer>=len(self.arr):
            self.pointer=len(self.arr)-1
            return self.arr[self.pointer]
        return self.arr[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)