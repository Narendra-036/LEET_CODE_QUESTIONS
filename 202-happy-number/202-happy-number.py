class Solution:
    def isHappy(self, num: int) -> bool:
        while True:
            ans=0
            num=str(num)
            for i in num:
                ans+=int(i)**2
            num=ans
            if num<10 :
                break
        if num==1 or num==7:
            return True
        return False
        
            