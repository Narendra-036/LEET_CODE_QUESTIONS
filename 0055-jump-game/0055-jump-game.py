class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        for j in range(len(nums)):
            if  j>i:
                return False
            i=max(i,j+nums[j])
        return True
    