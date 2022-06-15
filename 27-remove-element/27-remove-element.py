class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for j in range(len(nums)):
            if nums[j]==val:
                count+=1
                nums[j]=55
        nums.sort()
        return len(nums)-count
        
                