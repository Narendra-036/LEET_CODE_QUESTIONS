class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp, cur_dp = {(0,0):0}, defaultdict(lambda:float('inf'))
        for i, h in enumerate(houses):
            #g means the number of groups upto now
            for prev_color, g in dp:
                for cur_color in (range(1, n + 1) if not h else [h]):
                    cur_g = g + (prev_color != cur_color)
                    if cur_g > target: continue
                    cur_dp[cur_color, cur_g] = min(cur_dp[cur_color, cur_g], dp[prev_color,g]+(cost[i][cur_color-1] if cur_color != h else 0))
            dp, cur_dp = cur_dp, defaultdict(lambda:float('inf'))
        return min([dp[c, g] for c, g in dp if g == target] or [-1])