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
        print("x",x)
        
        ans=[]
        for i in reversed(sorted(x.keys())):
            print(i,x[i])
            ans.extend(x[i][::-1])    #{"i","love"}
        
        return ans[:k]