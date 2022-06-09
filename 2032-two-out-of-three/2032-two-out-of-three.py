class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans=[]
        a=max(len(nums1),len(nums2))
        
        for i in range(a):
            if i<len(nums1):
                if nums1[i] in nums2 or nums1[i] in nums3:
                    ans.append(nums1[i])
            if i<len(nums2):
                if nums2[i] in nums1:
                    continue
                if nums2[i] in nums3:
                    ans.append(nums2[i])
        ans=set(ans)
        ans=list(ans)
        return ans