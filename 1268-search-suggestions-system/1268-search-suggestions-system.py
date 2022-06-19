class Solution:
    def suggestedProducts(self, p: List[str], s: str) -> List[List[str]]:
        p.sort()
        a=[]
        for i in range(1,len(s)+1):
            b=[]
            count=0
            for j in range(len(p)):
                x=p[j]
                if s[:i] == x[:i]:
                    b.append(p[j])
                    count+=1
                if count==3:
                    break
            a.append(b)
        return a
            