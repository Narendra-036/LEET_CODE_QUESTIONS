class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        p=[]
        for i in nums:
            if i!=0:
                p.append(i)
        nums=p
        while nums:
            x=min(nums)
            for i in range(len(nums)):
                nums[i]-=x
            p=[]
            for i in nums:
                if i!=0:
                    p.append(i)
            nums=p
            count+=1
        return count