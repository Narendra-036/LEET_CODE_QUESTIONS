class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    a.append([i,j])
        for i in range(len(a)):
            j=a[i][0]
            k=0
            while k <len(matrix[0]):
                matrix[j][k]=0
                k+=1
            k=a[i][1]
            j=0
            while j<len(matrix):
                matrix[j][k]=0
                j+=1
            
                
            