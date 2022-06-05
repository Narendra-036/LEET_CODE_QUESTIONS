class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count=0
        self.n=n
        self.board=[["."]*n for _ in range(n)]
        self.solve(0)
        return self.count
        
    def check(self,row,col):
        for i in range(self.n):
            if self.board[i][col]=="Q":
                return False
            if row-i>=0 and col-i>=0 and self.board[row-i][col-i]=="Q":
                return False
            if row-i>=0 and col+i<self.n and self.board[row-i][col+i]=="Q":
                return False
        return True
    def solve(self,row):
        if row==self.n:
            self.count+=1
            return
        for j in range(self.n):
            if self.check(row,j):
                self.board[row][j]="Q"
                self.solve(row+1)
                
                self.board[row][j]="."
                
        