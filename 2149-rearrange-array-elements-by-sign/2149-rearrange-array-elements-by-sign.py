class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        b=[]
        a=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]<0:
                b.append(nums[i])
            else:
                a.append(nums[i])
        for i in range(len(a)):
            ans.append(a[i])
            ans.append(b[i])
        return ans