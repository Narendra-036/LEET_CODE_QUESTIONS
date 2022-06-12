class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            ans=0
            num=str(num)
            a=[i for i in num]
            for i in a:
                ans+=int(i)
            num=ans
        return num
            
            