class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            a.append(nums[nums[i]])
        return a