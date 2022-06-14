class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        a=[]
        while(i<len(nums)-1):
            if nums[i]==nums[i+1]:
                a.append(nums[i])
                i+=1
            i+=1
        return a
        