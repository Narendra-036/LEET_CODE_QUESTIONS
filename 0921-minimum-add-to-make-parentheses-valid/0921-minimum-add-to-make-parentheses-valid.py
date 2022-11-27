class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            
            stack.append(i)
            if len(stack)>=2:
                if stack[-2]=="(" and stack[-1]==')':
                    stack=stack[:-2]
        return len(stack)
                
            