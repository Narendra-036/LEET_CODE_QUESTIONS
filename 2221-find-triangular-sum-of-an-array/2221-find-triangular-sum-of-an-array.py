class Solution:
    def triangularSum(self, nums: List[int]) -> int:    
        while len(nums)>1:
            b=[]
            for i in range(1,len(nums)):
                b.append((nums[i]+nums[i-1])%10)
            nums=b
        return nums[0]
            