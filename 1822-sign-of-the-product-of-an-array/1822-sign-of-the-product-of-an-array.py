class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for i in nums:
            ans=ans*i
        if ans>0:
            return 1
        elif ans<0:
            return -1
        return 0