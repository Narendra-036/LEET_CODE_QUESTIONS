class Solution:
    def groupThePeople(self, q: List[int]) -> List[List[int]]:
        x={}
        for i in range(len(q)):
            if q[i] in x:
                x[q[i]].append(i)
            else:
                x[q[i]]=[i]
        
        ans=[]
        for i in x.keys():
            k=x[i]
            for j in range(0,len(x[i]),i):
                ans.append(k[j:j+i]) 
        return ans