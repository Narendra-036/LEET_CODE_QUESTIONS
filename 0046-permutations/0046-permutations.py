class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.check(nums,[],res)
        return res
    def check(self,nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.check(nums[:i]+nums[i+1:],path+[nums[i]],res)
        