class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        
        if k % 2 == 1 and len(nums) == 1:
            return -1
        
        if k > len(nums):
            return max(nums)
        
        if k == len(nums):
            return max(nums[:-1])
            
        return max(nums[:(k-1)] + [nums[k]])