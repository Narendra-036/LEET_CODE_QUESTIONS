class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            if n<0:
                n=0
            n+=nums[i]
            m=max(n,m)
        return m