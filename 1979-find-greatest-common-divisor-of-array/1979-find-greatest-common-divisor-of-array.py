class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        return gcd(x,y)
    
    
    
    
    def gcd(self,a,b):
        if (b == 0):
            return a
        return gcd(b, a%b)