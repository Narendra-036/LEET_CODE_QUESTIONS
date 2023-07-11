class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        # approach-------------------1
        
        
        # i=0
        # for _ in range(len(nums)):
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.append(0)
        #     else:
        #         i+=1
                        
            
#         approach 2-------------------------

        x=nums.count(0)
        for i in range(x):
            nums.remove(0)
            nums.append(0)
         
        
        