class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans=[]
        print(len(s))
        n_start=int(s[1])
        n_end=int(s[-1])
        for i in range(ord(s[0]),ord(s[3])+1):
            for j in range(n_start,n_end+1):
                d=str(chr(i))+str(j)
                ans.append(d)
        return ans