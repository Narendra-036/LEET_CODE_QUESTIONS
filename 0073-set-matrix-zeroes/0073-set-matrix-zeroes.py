class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x.append([i,j])
        for i in x:
            first=i[0]
            second=i[1]
            for k in range(0,len(matrix[0])):
                matrix[first][k]=0
            for k in range(0,len(matrix)):
                matrix[k][second]=0
                