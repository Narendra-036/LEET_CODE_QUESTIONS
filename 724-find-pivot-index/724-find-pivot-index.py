class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        lsum=0
        for i,x in enumerate(nums):
            if lsum==(s-lsum-x):
                return i
            lsum+=x
        return -1