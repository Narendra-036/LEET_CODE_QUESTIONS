class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        ans=0
        j=len(height)-1
        
        while i<j:
            x=min(height[i],height[j])*(j-i)
            ans=max(ans,x)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return ans