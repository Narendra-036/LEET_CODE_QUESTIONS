class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        
        x={}
        
        for i in reversed(sorted(d.keys())):
            
            if d[i] in x:
                x[d[i]].append(i)
            else:
                x[d[i]]=[i]
        
        ans=[]
        for i in reversed(sorted(x.keys())):
            ans.extend(x[i][::-1])
        
        return ans[:k]