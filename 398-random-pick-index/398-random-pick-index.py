
class Solution:

    def __init__(self, nums: List[int]):
        self.index=defaultdict(list)
        self.arr=nums
        for i,num in enumerate(nums):
            self.index[num].append(i)
            
            

    def pick(self, target: int) -> int:
        return random.choice(self.index[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)