class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i=3
        
        ans=sum(arr)
        
        while i <=len(arr):
            
            for k in range(len(arr)-i+1):
                
                ans+=sum(arr[k:k+i])
            
            i+=2
        
        return ans