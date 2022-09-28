class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        count=0
        n=sorted(list(set(nums)))
        for i in range(len(n)):
            if n[i] <= k:
                count+=n[i]
                k+=1
        return k*(k+1)//2 - count