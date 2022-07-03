class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        d=nums[1]-nums[0]
        count=0
        if d!=0:
            count=2
        else:
            count=1
        for i in range(2,len(nums)):
            x=nums[i]-nums[i-1]
            if (x>0 and d<=0) or (x<0 and d>=0):
                count+=1
                d=x
        return count