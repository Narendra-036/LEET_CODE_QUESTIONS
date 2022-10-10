class Solution:
    def breakPalindrome(self, s: str) -> str:
        
        def palin(s):
            i=0
            j=len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        if len(s)==1:
            return ""
        else:
            # st=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            x=""
            if len(s)==s.count("a"):
                return s[:-1]+"b"
            for i in range(len(s)):
                if s[i]!="a":
                    x=s[:i]+"a"+s[i+1:]
                    if palin(x):
                        continue
                    else:
                        return x
            if palin(x):
                return s[:-1]+"b"
            
            