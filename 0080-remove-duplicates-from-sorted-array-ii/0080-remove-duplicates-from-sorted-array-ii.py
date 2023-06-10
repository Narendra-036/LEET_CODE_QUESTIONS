class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        s=set(nums)
        for i in s:
            x=nums.count(i)
            if x>2:
                c+=2
                for j in range(x-2):
                    nums.remove(i)
            else:
                c+=x
        return c