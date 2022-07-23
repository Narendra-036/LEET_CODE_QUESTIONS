from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rslts = [None]*n
        sl = SortedList()
        for i in reversed(range(n)):
            rslts[i] = sl.bisect_left(nums[i])
            sl.add(nums[i])
        return rslts