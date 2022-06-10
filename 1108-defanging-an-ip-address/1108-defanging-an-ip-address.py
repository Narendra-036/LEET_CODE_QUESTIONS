class Solution:
    def defangIPaddr(self, address: str) -> str:
        x,y,a,b=map(str,address.split("."))
        ans=x+"[.]"+y+"[.]"+a+"[.]"+b
        return ans