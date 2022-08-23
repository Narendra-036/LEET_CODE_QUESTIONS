class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st = ''.join(ch for ch in s if ch.isalnum())
        i=0
        j=len(st)-1
        while i<j:
            if st[i]==st[j]:
                i+=1
                j-=1
            else:
                return False
        return True