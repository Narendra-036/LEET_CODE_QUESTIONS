class Solution:
    def simplifyPath(self, path: str) -> str:
        i=0
        j=1
        k=1
        stack=[]
        while k<len(path):
            if path[k]=="/":
                i=k
                stack.append(path[j:i])
                j=i+1
                if stack and stack[-1]=="":
                    stack.pop(-1)
                if stack and stack[-1]==".":
                    stack.pop(-1)
                if stack and stack[-1]=="..":
                    stack=stack[:-2]
            k+=1
        if i<len(path)-1:
            stack.append(path[i+1:])
        if not stack:
            return "/"
        if stack and stack[-1]==".":
            stack.pop(-1)
        if stack and stack[-1]=="..":
            stack=stack[:-2]
        return "/"+"/".join(stack)
        print(stack)
            
    