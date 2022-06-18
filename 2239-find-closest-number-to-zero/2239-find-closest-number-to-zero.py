class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=999999
        k=0
        for i in range(len(nums)):
            if abs(0-nums[i])<=ans:
                ans=abs(0-nums[i])
                k=nums[i]
        return k