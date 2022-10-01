class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=nums[0]
        m=nums[0]
        for i in nums[1:]:
            if n<0:
                n=0
            n+=i
            m=max(n,m)
        return m