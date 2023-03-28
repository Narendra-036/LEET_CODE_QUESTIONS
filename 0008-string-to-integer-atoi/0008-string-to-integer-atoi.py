class Solution:
    def myAtoi(self, s: str) -> int:
        ans=[]
        for i in s:
            if (ord(i)==45 or ord(i)==43)  and not ans:
                ans.append(i)
            elif ord(i)>=48 and ord(i)<=57:
                ans.append(i)
            elif ord(i)==32 and not ans:
                continue
            elif ord(i)==32 and ans:
                break
            else:
                break
    
        s=""
        s="".join(ans)
        print(s)
        if len(s)==0:
            return 0
        if len(s)==1 and (s[0]=="+" or s[0]=="-"):
            return 0
        if int(s)<=2147483647 and int(s)>=-2147483648:
            
            return int(s)
        else:
            if s[0]=="-":
                return -2147483648
            else:
                return 2147483647

                
    
    
        
            
        
        
