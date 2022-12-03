class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        
        x={}
        for i in d:
            if d[i] in x:
                x[d[i]].append(i)
            else:
                x[d[i]]=[i]
        ans=""
        for i in reversed(sorted(x.keys())):
            for j in range(len(x[i])):
                ans+=x[i][j]*i
        return ans