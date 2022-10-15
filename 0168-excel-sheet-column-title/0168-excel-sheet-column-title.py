class Solution:
    def convertToTitle(self, x: int) -> str:
        ans=""
        while x!=0:
            a=x%26
            if a==0:
                a=26
            x=x-a
            
            ans+=chr(64+int(a))
            x=x//26
        return ans[::-1]
        