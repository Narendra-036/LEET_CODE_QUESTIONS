class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        max_len, total = 0, 0
        N = len(nums)
        if target == 0:
            return N
        i, j = 0, 0
        while i < N:            
            if total + nums[i] > target and j < i:
                total -= nums[j]
                j += 1
            else:
                total += nums[i]
                i += 1
            if total == target:
                max_len = max(max_len, i - j + 1)
        
        return -1 if max_len == 0 else N - max_len + 1