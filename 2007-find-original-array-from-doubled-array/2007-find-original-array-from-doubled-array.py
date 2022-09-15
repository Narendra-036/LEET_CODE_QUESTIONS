class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return [] 
        d=Counter(changed)
        

        ans=[]
        n=len(changed)

        for k in sorted(d.keys()):
            if d[k]!=0:
                if k==0 and d[k]&1:
                    
                    return []
                ans += [k] * (d[k] // 2 if k == 0 else d[k])
                d[2*k] -= d[k]
            d[k] = 0 
        if any(v !=0 for v in d.values()):
            return []
        return ans
