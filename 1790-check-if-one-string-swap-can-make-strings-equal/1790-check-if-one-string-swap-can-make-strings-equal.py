class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        check=0
        s=[i for i in s1]
        x=[i for i in s2]
        s.sort()
        x.sort()
        print(s,x)
        if s!=x:
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                check+=1
        if check==2 or check==0:
            return True
        return False