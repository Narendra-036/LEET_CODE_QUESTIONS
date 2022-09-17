class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            arr.append(i)
            if len(arr)>1:
                if arr[-1]=="]" and arr[-2]=="[":
                    arr.pop()
                    arr.pop()
                    continue
                if arr[-1]==")" and arr[-2]=="(":
                    arr.pop()
                    arr.pop()
                    continue
                if arr[-1]=="}" and arr[-2]=="{":
                    arr.pop()
                    arr.pop()
                    continue
        if arr:
            return False
        return True