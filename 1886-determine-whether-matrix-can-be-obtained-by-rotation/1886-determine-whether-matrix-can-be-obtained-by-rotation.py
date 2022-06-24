class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        
        
        o=0
        while o<4:
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
            if matrix==target:
                return True
            o+=1
        return False