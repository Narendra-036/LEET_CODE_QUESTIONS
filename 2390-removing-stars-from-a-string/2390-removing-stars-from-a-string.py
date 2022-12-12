class Solution:
    def removeStars(self, s: str) -> str:
        x=[]
        for i in s:
            x.append(i)
            while len(x)>0 and x[-1]=="*":
                x.pop(-1)
                x.pop(-1)
        return "".join(x)
    
    
        # while "*" in s:
        #     for i in range(len(s)):
        #         if s[i]=="*":
        #             s=s[:i-1]+s[i+1:]
        #             break
        # return s