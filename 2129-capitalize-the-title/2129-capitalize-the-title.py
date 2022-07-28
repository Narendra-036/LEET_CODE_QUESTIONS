class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=list(map(str,title.split()))
        ans=""
        for i in x:
            s=i.lower()
            if len(s)>2:
                
                s=s[0].upper()+s[1:]
            ans+=s
            ans+=" "
            
        return ans[:-1]