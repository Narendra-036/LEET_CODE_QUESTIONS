class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ans=0
        a=1000000
        for i in range(n):
            a=min(a,prices[i])
            if prices[i]-a>ans:
                ans=prices[i]-a

        return ans