class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        end = int(sqrt(c)) + 1       
        for b in range(end):    
            a = sqrt(c-b*b)     
            if int(a) == a:     
                return True
        return False
                
        