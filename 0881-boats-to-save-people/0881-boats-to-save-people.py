class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        i,j =0, len(p)-1
        ans=0
        while i<=j:
            ans+=1
            if p[i]+p[j]<=limit:
                i+=1
            j-=1
        return ans