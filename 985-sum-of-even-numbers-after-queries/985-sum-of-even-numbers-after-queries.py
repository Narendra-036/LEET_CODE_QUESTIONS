class Solution:
    def sumEvenAfterQueries(self, nums: List[int], x: List[List[int]]) -> List[int]:
        ans=[]
        a=0
        for j in nums:
            if j%2==0:
                a+=j 
                
        sm=a
        for i in x:
            a=sm
            temp=nums[i[1]]
            
            nums[i[1]]+=i[0]
            if temp%2==0 and nums[i[1]]%2==0:
                a=a-temp+nums[i[1]]
                
            elif temp%2==0 and nums[i[1]]%2!=0:
                a=a-temp
            elif temp%2!=0 and nums[i[1]]%2==0:
                a+=nums[i[1]]
                
            else:
                pass
            sm=a
            
            
            ans.append(a)
        return ans
                    