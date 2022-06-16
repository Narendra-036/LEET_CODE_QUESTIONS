class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        b=[]
        a=[]
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                b.append(nums[i])
            else:
                a.append(nums[i])
        a.sort()
        a.reverse()
        b.sort()
        x=max(len(a),len(b))
        for i in range(x):
            if i<len(b):
                ans.append(b[i])
            if i<len(a):
                ans.append(a[i])
        
            
        return ans