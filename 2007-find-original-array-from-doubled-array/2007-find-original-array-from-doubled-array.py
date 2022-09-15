class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return [] # since changed is not a double-array then

        d=Counter(changed)
        """for c in changed:
            d[c]=d.get(c,0)+1"""

        ans=[]
        n=len(changed)

        for k in sorted(d.keys()):
            if d[k]!=0:
                if k==0 and d[k]&1:
                    # x&1 is a fast way to check if a number x is odd/even.
                    # It is the same as x%2==1 but it's faster.
                    return []
                ans += [k] * (d[k] // 2 if k == 0 else d[k])
                d[2*k] -= d[k]
            d[k] = 0 
        if any(v !=0 for v in d.values()):
            return []
        return ans
