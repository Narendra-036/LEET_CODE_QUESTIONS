class Solution:
    def largestWordCount(self, m: List[str], s: List[str]) -> str:
        d={}
        for i in range(len(s)):
            x=list(map(str,m[i].split(" ")))
            x=len(x)
            if s[i] not in d:
                d[s[i]]=x
            else:
                d[s[i]]+=x
        x={}
        for i in d:
            if d[i] not in x:
                x[d[i]]=[i]
            else:
                x[d[i]].append(i)
        ans=[]
        for i in reversed(sorted(x.keys())):
            ans=x[i]
            ans.sort()
            break
        return ans[-1]