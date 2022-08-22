class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        c = 1
        d = dict()
        for i in sorted(list(set(arr))):
            d[i] = c
            c += 1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr