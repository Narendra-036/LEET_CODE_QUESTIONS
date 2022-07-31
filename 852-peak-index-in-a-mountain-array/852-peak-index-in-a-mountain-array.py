class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binarysearch(l,r):
            mid = (l+r)//2
            
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                return binarysearch(l,mid)
            elif arr[mid] < arr[mid+1]:
                return binarysearch(mid,r)
        return binarysearch(0,len(arr)-1)