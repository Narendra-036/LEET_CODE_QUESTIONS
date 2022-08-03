class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            print("a")
            x=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    x=j
            if x==len(nums2)-1:
                ans.append(-1)
                continue
            for k in range(x+1,len(nums2)):
                if nums1[i]<nums2[k]:
                    ans.append(nums2[k])
                    break
            
            if len(ans)==i+1:
                continue
            ans.append(-1)
            
        return ans