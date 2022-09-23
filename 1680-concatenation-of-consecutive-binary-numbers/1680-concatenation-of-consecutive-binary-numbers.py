class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=""
        for i in range(1,n+1):
            ans+=str(bin(i)[2:])
        
        x=int(ans,2)
        return x%((10**9)+7)