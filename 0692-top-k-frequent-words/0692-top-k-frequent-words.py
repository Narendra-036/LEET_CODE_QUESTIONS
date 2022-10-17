class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x={}
        
        # y=dict(sorted(d.items(), key=lambda item: item[1]))
        for i in reversed(sorted(d.keys())):
            if d[i] in x:
                x[d[i]].append(i)
            else:
                x[d[i]]=[i]
        
        ans=[]
        for i in reversed(sorted(x.keys())):
            ans.extend(x[i][::-1])
            
        return ans[:k]
        