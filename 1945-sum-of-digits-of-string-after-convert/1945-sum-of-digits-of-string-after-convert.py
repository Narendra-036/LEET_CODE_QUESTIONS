class Solution:
    def getLucky(self, s: str, k: int) -> int:
        import string
        case = dict(zip(string.ascii_lowercase, range(1,27)))
        
        a=""
        for i in s:
            a+=str(case[i])
        
        
        ans=0
        for i in range(k):
            for j in a:
                ans+=int(j)
            a=str(ans)
            ans=0
        return int(a)