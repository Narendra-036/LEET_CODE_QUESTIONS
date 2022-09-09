class Solution:
    def numberOfWeakCharacters(self, arr: List[List[int]]) -> int:
        count=0
        m=0
        arr.sort(key=lambda x: (-x[0], x[1]))
        for _, i in arr:
            if i<m:
                count+=1
            else:
                m=i
        return count