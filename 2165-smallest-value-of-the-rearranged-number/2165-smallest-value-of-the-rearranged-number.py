class Solution:
    def smallestNumber(self, num: int) -> int:
        s=str(num)
        a=[]
        ans=""
        if num<0:
            a=[i for i in s[1:]]
            a.sort()
            a.reverse()
            for i in a:
                ans+=i
            return("-"+ans)
        else:
            a=[i for i  in s]
            a.sort()
            j=0
            for i in range(len(a)):
                if a[i]=="0":
                    continue
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                break
            for i in a:
                ans+=i
            return ans