class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxD = 0                            
        i = j = 0                           

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:         
                i += 1                      
            else:                           
                maxD = max(maxD, j-i)       
                j += 1                      
        
        return maxD