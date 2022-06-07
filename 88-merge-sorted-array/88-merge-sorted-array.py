class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans=(nums1[:m]+nums2[:n])
        ans.sort()
        
        for i in range(len(nums1)):
            nums1[i]=ans[i]
            
        
        