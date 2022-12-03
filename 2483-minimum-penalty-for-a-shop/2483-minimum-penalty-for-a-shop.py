class Solution:
    def bestClosingTime(self, c: str) -> int:
        
        c=[i for i in c]
        ans=c.count("Y")   
        x=0
        check=ans
        if ans:
            for i in range(len(c)):
                if c[i]=="Y":
                    c[i]="N"
                    check-=1
                    k=check
                else:
                    c[i]="Y"
                    check+=1
                    k=check
                if k<ans:
                    ans=k
                    x=i+1
        return x