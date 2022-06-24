class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        i=0
        nums=str(num)
        while(i<len(nums)-k+1):
            if int(nums[i:k+i])!=0 and  num%int(nums[i:k+i])==0 :
                count+=1
            i+=1
        return count