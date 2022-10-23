class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = list(set(range(1, n + 1)) - set(nums))[0]
        duplicate = missing + sum(nums) - (n + 1) * n // 2
        return [duplicate, missing]