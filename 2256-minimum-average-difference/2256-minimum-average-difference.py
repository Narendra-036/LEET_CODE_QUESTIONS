class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        mini=float('inf')
        ans=0
        for i in range(len(nums)):
            left+=nums[i]
            right-=nums[i]
            x=left//(i+1)
            if right==0:
                y=0
            else:
                y=right//(len(nums)-(i+1))
            if abs(x-y)<mini:
                mini=abs(x-y)
                ans=i

        return ans