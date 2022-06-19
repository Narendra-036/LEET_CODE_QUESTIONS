class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        x=0
        while i<len(nums):
            x+=min(nums[i],nums[i+1])
            i+=2
        return x