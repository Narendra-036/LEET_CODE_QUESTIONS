class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            
            s=[int(i) for i in s]
            x=""
            for i in range(0,len(s),k):
                x+=str(sum(s[i:i+k]))
            s=x
        return s
                
            