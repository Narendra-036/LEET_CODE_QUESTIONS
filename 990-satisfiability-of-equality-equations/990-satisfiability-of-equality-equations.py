class UF:
    def __init__(self):
        self.arr = list(range(26))

    def charToInt(self,c):
        return ord(c) - ord('a')

    def find(self,x): 
        x = self.charToInt(x)
        curr = self.arr
        while curr[x] != x:
            x = curr[x]
        return curr[x]

    def union(self,x,y): 
        curr = self.arr
        curr[self.find(x)] = self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UF()
        for e in equations: 
            first,indicator,equal,second = e
            if indicator == "=":
                uf.union(first,second)

        for e in equations:
            first,indicator,equal,second = e
            if indicator == "!":
                if uf.find(first) == uf.find(second):
                    return False
        return True