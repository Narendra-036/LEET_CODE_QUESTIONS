class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n%2!=0:
            ans=[0]
        if n//2==0:
            return ans
        i=1
        while i<=n//2:
            ans.append(i)
            ans.append(-i)
            i+=1
        return ans