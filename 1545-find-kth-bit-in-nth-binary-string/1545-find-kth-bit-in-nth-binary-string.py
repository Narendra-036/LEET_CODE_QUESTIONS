class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n):
            
            x=""
            for i in s:
                if i=="0":
                    x+="1"
                else:
                    x+="0"

            s=s+'1'+x[::-1]
            if len(s)>k-1:
                return s[k-1]

        