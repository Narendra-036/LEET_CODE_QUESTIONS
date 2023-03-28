class Solution:
    def myAtoi(self, ks: str) -> int:
        s=""
        for i in ks:
            if (ord(i)==45 or ord(i)==43)  and len(s)==0:
                # ans.append(i)
                s+=i
            elif ord(i)>=48 and ord(i)<=57:
                # ans.append(i)
                s+=i
            elif ord(i)==32 and len(s)==0:
                continue
            elif ord(i)==32 and len(s)!=0:
                break
            else:
                break
    
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

                
    
    
        
            
        
        
