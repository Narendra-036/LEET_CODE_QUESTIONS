class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 1e5
        ans = 1e5
        
        for i in range(0 , len(nums) - 2):   
            if i == 0 or nums[i] != nums[i-1]:
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    temp = nums[i] + nums[low] + nums[high]
                    if abs(target - temp) < min_diff:
                        min_diff = abs(target - temp)
                        ans = temp
                    if temp == target:
                        return target
                    elif temp < target:
                        low += 1
                    else:
                        high -= 1
        return ans