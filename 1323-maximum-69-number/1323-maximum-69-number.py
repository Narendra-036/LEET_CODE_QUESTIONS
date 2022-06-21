class Solution:
    def maximum69Number (self, num: int) -> int:
        num=[i for i in str(num)]
        print(num)
        for i in range(len(num)):
            if num[i]=="6":
                num[i]="9"
                break
        ans=0
        for i in num:
            ans+=int(i)
            ans*=10
        return ans//10