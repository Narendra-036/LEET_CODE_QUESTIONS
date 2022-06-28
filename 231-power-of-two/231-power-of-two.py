import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # x=math.log(n,2)
        # print(x)
        # if x==int(x):
        #     return True
        # return False
        return n and not (n & n - 1)