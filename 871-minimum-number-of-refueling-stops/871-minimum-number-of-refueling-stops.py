class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q=[]
        stations.append((target,float('inf')))
        ans=0
        x=0
        for i,j in stations:
            startFuel-=i-x
            while q and startFuel<0:
                startFuel+= -heapq.heappop(q)
                ans+=1
            if startFuel<0: return -1
            heapq.heappush(q,-j)
            x=i
        return ans