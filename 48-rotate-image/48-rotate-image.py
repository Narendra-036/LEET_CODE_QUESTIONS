class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        k=len(matrix)-1
        a=[]
        for i in range(len(matrix)):
            b=[]
            for j in range(len(matrix)):
                b.append(matrix[i][j])
            a.append(b)
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                
                matrix[j][k]=a[i][j]
                
            k-=1