class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c ==len(mat)*len(mat[0]):
            a=[]
            ans=[]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    a.append(mat[i][j])
            i=0
            while(i<len(a)):
                ans.append(a[i:i+c])
                i+=c
            return ans
        return mat