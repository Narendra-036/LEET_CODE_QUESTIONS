class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x=set(nums1)
        x=list(x)
        y=set(nums2)
        y=list(y)
        a=[]
        ans=[[],[]]
        for i in x:
            if i in y:
                a.append(i)
        for i in range(max(len(x),len(y))):
            if i<len(x) and x[i] not in a:
                ans[0].append(x[i])
            if i<len(y) and y[i] not in a:
                ans[1].append(y[i])
        return ans