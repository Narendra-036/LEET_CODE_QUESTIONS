class TextEditor:

    def __init__(self):
        self.cursor=0
        self.text=""

    def addText(self, text: str) -> None:
        self.text=self.text[:self.cursor]+text+self.text[self.cursor:]
        self.cursor+=len(text)
    def deleteText(self, k: int) -> int:
        # print(self.text)
        x=len(self.text)
        if k>self.cursor:
            k=self.cursor
        self.text=self.text[:self.cursor-k]+self.text[self.cursor:]
        self.cursor-=k
        return x-len(self.text)

    def cursorLeft(self, k: int) -> str:
        
        self.cursor-=k
        if self.cursor<0:
            self.cursor=0
        if not self.cursor:
            return ""
        return self.text[self.cursor-min(10,self.cursor):self.cursor]
    
            

    def cursorRight(self, k: int) -> str:
        self.cursor+=k
        if self.cursor>=len(self.text):
            self.cursor=len(self.text)
        if self.cursor==len(self.text):
            
            return self.text[-10:]
        # print(self.cursor)
        return self.text[self.cursor-min(10,self.cursor):self.cursor]
            


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)