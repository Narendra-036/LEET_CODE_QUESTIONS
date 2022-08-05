class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
    
        while n>0:
            c=0 
            for num in nums:
                if num>=n:
                    c+=1
            if c==n:
                return n
            n-=1
        return -1