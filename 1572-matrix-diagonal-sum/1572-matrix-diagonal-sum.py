class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        a=len(mat)-1
        for i in range(len(mat)):
            sum+=mat[i][i]
            sum+=mat[i][a]
            print(sum)
            a-=1
        if len(mat)%2==0:
            return sum
        else:
            b=len(mat)//2
            sum-=mat[b][b]
            return sum
            