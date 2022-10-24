class Solution:
    def maxLength(self,arr):

        unique = ['']
        res = 0
        for i in range(len(arr)):
            for j in range(len(unique)):
                
                local = arr[i]+unique[j]
                
                if len(local)==len(set(local)):
                    unique.append(local)
                    
                    res=max(res,len(local))
                    
        return res