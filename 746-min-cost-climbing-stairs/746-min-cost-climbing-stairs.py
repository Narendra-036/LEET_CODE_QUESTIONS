class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        temp={0:0,1:0}
        def help(n):
            if n in temp:
                return temp[n]
            else:
                temp[n]=min((help(n-1)+cost[n-1]),(help(n-2)+cost[n-2]))
                return temp[n]
        return help(len(cost))