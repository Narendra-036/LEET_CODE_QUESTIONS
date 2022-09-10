class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = defaultdict(int)
        l = len(prices)
        
        def find(i,j):
            nonlocal k, l
            if i>=l or j>=2*k:
                return 0
            
            if (i,j) not in dp:
                if j%2==0:
                    dp[i,j] = max(-prices[i] + find(i+1, j+1), find(i+1, j))
                else:
                    dp[i,j] = max(prices[i] + find(i+1, j+1), find(i+1, j))
                    
            return dp[i,j]
        
        return find(0, 0)