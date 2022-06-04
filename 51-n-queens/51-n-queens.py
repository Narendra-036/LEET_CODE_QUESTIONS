class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans=[]
        self.n=n
        self.board= [["."] * n for _ in range(n)]
        self.solve(0)
        return self.ans
    
        
    def check(self,row,col):
        n=len(self.board)
        for i in range(n):
            
            if self.board[i][col]=="Q":
                return False
            
            if row-i>=0 and col-i>=0 and self.board[row-i][col-i]=="Q":
                return False
            
            if row-i>=0 and col+i<len(self.board) and self.board[row-i][col+i]=="Q":
                return False
        return True
    def solve(self,row):
        if row==self.n:
            b=[]
            for k in self.board:
                str=""
                for l in k:
                    str+=l
                b.append(str)
            self.ans.append(b)
            return
            
            
        for i in range(self.n):
            if self.check(row,i):
                self.board[row][i]="Q"
                
                self.solve(row+1)
                self.board[row][i]="."
    
    