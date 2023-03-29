class Solution:
    def insert(self, c: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        c.append(newInterval)
        c=sorted(c,key=lambda x:x[0])
        ans=[c[0]]
        for i in c[1:]:
            if i[0]<=ans[-1][1]:
                ans[-1]=[min(ans[-1][0],i[0]),max(ans[-1][1],i[1])]
            else:
                ans.append(i)
        return ans