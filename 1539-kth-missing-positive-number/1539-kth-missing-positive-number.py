class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x={i for i in range(1,100000)}
        for i in arr:
            x.remove(i)
        x=list(x)
        x.sort()
        
        return x[k-1]