class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        d={}
        for i in m:
            if i[0] in d:
                d[i[0]][0]+=1
            if i[1] in d:
                d[i[1]][1]+=1
            if i[0] not in d:
                d[i[0]]=[1,0]
            if i[1] not in d:
                d[i[1]]=[0,1]
            
        a=[]
        b=[]
        for i in d:
            if d[i][1]==0:
                a.append(i)
            if d[i][1]==1:
                b.append(i)
        ans=[]
        a.sort()
        b.sort()
        ans.append(a)
        ans.append(b)
        
        return ans