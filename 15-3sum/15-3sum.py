class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif  nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r - 1 and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1     
        return triplets