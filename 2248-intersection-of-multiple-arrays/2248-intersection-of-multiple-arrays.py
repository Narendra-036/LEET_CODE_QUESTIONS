class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        ans=[]
        for i in range(len(nums[0])):
            a=nums[0][i]
            count=0
            for j in range(len(nums)):
                if a in nums[j]:
                    count+=1
            if count==len(nums):
                ans.append(a)
        ans.sort()
        return ans