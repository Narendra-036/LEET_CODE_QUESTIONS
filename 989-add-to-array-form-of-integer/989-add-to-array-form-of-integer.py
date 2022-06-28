class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s+=str(i)
        num=str(int(s)+k)
        
        ans=[i for i in num]
        return ans