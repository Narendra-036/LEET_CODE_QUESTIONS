class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k%2==1:
            return -1
        ans=0
        if k==0:
            return nums[0]
        while nums and k>1:
            ans=max(ans,nums.pop(0))
            k-=1
    
        if k==1 and len(nums)>1:
            return max(ans,nums[1])
        elif k==1:
            return ans
        else:
            return ans
        print(k, ans, nums)