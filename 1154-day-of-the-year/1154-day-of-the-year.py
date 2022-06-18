class Solution:
    def dayOfYear(self, date: str) -> int:
        x=list(map(str,date.split("-")))
        y=[31,28,31,30,31,30,31,31,30,31,30,31]
        ans=0
        a=int(x[0])
        if (a%400==0 or (a%4==0 and a%100!=0)) and int(x[1])>2:
            
            ans=1
        ans+=sum(y[:int(x[1])-1])+int(x[2])
        return ans
        