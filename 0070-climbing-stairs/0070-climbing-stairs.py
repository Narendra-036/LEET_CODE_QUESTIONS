class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[1,2,3,5]
        for i in range(n-4):
            arr.append(arr[-1]+arr[-2])
        return arr[n-1]