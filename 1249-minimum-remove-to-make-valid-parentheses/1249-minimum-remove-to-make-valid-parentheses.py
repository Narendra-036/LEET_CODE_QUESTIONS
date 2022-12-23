class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        check=[]
        for i in range(len(s)):
            if s[i]=="(":
            
                stack.append('(')
                check.append(i)
            if s[i]==")":
                stack.append(")")
                check.append(i)
            
            # print(stack)
            while len(stack)>=2 and stack[-1]==")" and stack[-2]=="(":
                stack.pop(-1)
                stack.pop(-1)
                check.pop(-1)
                check.pop(-1)
                # print(check)
        ans=""
        for i in range(len(s)):
            if i  not in check:
                ans+=s[i]
        return ans