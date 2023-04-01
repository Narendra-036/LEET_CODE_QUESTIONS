class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        x=1
        for i in nums[::-1]:
            x=x*i
            ans.append(x)
        ans=ans[::-1]
        # print(ans)
        x=1
        for i in range(len(nums)):
            
            if i==0:
                x*=nums[i]
                ans[i]=ans[i+1]
                # print(x)
                
                
            elif i==len(nums)-1:
                ans[i]=x
                # print(x)
                
                
            else:
            
                ans[i]=x*ans[i+1]
                x*=nums[i]
                
                
        #     print(ans)
        # print(ans)
        
        
        return ans