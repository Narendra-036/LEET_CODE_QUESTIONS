class Solution:
    def breakPalindrome(self, s: str) -> str:
        
        
        
        #checking for palindrome... 
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
        
        #stats.....................
        if len(s)==1:
            return ""
        
        else:
            
            
            
            # st=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            x=""
            for i in range(len(s)):
                if s[i]!="a":
                    
                    #changing the current element with a
                    x=s[:i]+"a"+s[i+1:]
                    
                    
                    
                    #checking palindrome after changing
                    if palin(x):
                        continue
                    else:
                        return x
                    
            #if it is still palindrome then change the last letter....\U0001f44d
            if palin(x):
                return s[:-1]+"b"
            
#HAPPY CODING...\U0001f973\U0001f973\U0001f973\U0001f973\U0001f973
            
            