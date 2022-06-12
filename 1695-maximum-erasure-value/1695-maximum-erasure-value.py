class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a=set()
        total=0
        ans=0
        j=0
        for i in range(len(nums)):
            x=nums[i]
            while j<i and x in a:
                a.remove(nums[j])
                
                total-=nums[j]
                j+=1
            a.add(nums[i])
            total+=nums[i]
            ans=max(ans,total)
        return ans