class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        
        def solve(n, k, target, currSum, currDie):
            if currSum == target:
                if currDie == n: return 1
                return 0
            
            if currDie == n: return 0
            if currSum > target: return 0
            if (currSum, currDie) in dp: return dp[(currSum, currDie)]
            
            res = 0
            
            for i in range(1, k + 1):
                res += solve(n, k, target, currSum + i, currDie + 1)
            
            dp[(currSum, currDie)] = res
            return res
        
        return solve(n, k, target, 0, 0) % (10 ** 9 + 7)