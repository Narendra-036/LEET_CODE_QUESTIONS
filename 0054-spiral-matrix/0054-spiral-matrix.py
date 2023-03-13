class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res=[]
        while m:
            if m:
                res+=m.pop(0)
            if m and m[0]:
                for row in m:
                    res.append(row.pop())
            if m:
                res+=m.pop(-1)[::-1]
            if m and m[0]:
                for row in m[::-1]:
                    res.append(row.pop(0))
        return res
            
            
            