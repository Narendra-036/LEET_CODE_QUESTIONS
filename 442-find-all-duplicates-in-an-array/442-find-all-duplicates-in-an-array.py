class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        j=1
        k=2
        a=[]
        if len(nums)==2:
            if nums[0]==nums[1]:
                return [nums[0]]
            else:
                return []
        while i<len(nums) and j<len(nums):
            if nums[i]==nums[k]:
                a.append(nums[i])
                i=k+1
                j=i+1
                k=j+1
            elif nums[i]==nums[j]:
                a.append(nums[i])
                i=j+1
                j=i+1
                k=j+1
                
            else:
                i+=1
                j+=1
                k+=1
            if k>len(nums)-1:
                k=0
                
        return a
        