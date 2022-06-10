class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        y=str(x)
        y=y[::-1]
        if y==str(x):
            return True
        return False
        