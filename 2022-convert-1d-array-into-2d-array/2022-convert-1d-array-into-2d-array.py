class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        if m*n==len(original):
            i=0
            x=0
            while(x<m):
                ans.append(original[i:i+n])
                i+=n
                x+=1
        return ans
        