class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=defaultdict(list)
        for i in range(len(arr)):
            x[arr[i]].append(i)
        c=-2
        for i in x:
            if i==len(x[i]):
                c=max(c,i)
        return max(c,-1)
                