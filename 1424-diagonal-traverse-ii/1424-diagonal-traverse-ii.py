class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagsums = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j in diagsums:
                    diagsums[i+j].insert(0,nums[i][j])
                else:
                    diagsums[i+j] = [nums[i][j]]
                    
        out = []
        for k, v in diagsums.items():
            out+=v
        
        return out