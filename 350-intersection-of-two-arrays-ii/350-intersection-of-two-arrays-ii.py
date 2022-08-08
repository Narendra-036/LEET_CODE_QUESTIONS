class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        a=[False]*len(nums2)
        ans=[]
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j] and a[j]==False:
                    ans.append(i)
                    a[j]=True
                    break
        return ans