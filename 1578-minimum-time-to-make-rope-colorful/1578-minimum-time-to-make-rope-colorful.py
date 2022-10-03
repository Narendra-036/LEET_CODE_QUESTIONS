class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        t=0
        i=0
        j=0
        while i<len(neededTime) and j<len(neededTime):
            cur=0
            m=0
            while j<len(neededTime) and colors[i]==colors[j]:
                cur+=neededTime[j]
                m=max(m,neededTime[j])
                j+=1
            t+=cur-m
            i=j
        return t