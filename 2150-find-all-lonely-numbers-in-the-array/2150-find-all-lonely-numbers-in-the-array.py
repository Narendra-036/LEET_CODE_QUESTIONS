class Solution:
    def findLonely(self, n: List[int]) -> List[int]:
        x={}
        for i in n:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        ans=[]
        for i in x:
            if x[i]>1:
                continue
            if i-1 in x:
                continue
            if i+1 in x:
                continue
            ans.append(i)
        return ans