class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        b=[]
        a=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                b.append(nums[i])
            else:
                a.append(nums[i])
        for i in range(len(a)):
            ans.append(b[i])
            ans.append(a[i])
        return ans