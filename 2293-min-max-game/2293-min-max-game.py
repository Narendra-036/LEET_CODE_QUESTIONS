class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            c=[]
            i=0
            j=1
            count=0
            while j<len(nums):
                if count%2==0:
                    c.append(min(nums[i],nums[j]))
                else:
                    c.append(max(nums[i],nums[j]))
                i+=2
                j+=2
                count+=1
            nums=c
            
        return nums[0]