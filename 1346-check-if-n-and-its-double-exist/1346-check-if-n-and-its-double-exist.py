class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if arr.count(0)>1:
            return True
        if arr.count(0)==1:
            arr.remove(0)
        for i in arr:
            if i*2 in arr:
                return True
        return False