class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        n=set(nums)
        for i in n:
            if i-1 not in n:
                c=i
                cs=1
                while c+1 in n:
                    c+=1
                    cs+=1
                ans=max(ans,cs)
        return ans