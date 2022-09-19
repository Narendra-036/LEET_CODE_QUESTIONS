class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.ranges, low = [], 0
        for i in sorted(blacklist + [n]):
            self.ranges += ((low, i - 1),) if low != i else ()
            low = i + 1

    def pick(self):
        return randint(*choice(self.ranges))


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()