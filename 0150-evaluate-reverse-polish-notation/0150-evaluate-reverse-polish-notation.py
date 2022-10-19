class Solution:
    def evalRPN(self, t: List[str]) -> int:
        x=[]
        i=0
        check=["+","-","*","/"]
        for j in  t:
            x.append(j)
            if x[-1] in check:
                v=0
                a=int(x[-3])
                b=int(x[-2])
                if x[-1]=="+":
                    v=a+b
                elif x[-1]=="-":
                    v=a-b
                elif x[-1]=="*":
                    v=a*b
                else:
                    v=a/b
                x=x[:-3]
                x.append(v)
                
        return int(x[-1])