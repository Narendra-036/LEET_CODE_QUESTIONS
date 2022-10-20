import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums[:]
        self.nums=nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.arr)
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()