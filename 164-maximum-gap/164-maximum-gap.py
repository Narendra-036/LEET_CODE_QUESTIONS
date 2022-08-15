class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        dif=0
        nums.sort()
        for i in range(1,len(nums)):
            dif =max(dif,abs(nums[i]-nums[i-1]))
        return dif