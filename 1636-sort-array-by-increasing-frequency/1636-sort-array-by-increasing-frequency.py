class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        
        counts_dict = Counter(nums)
        return sorted(nums, key = lambda x: (counts_dict[x], -x))
    
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # x={}
        # for i in d:
        #     if d[i] not in x:
        #         x[d[i]]=[i]
        #     else:
        #         x[d[i]].append(i)
        # print(x)
        # ans=[]
        # for i in sorted(x):
        #     for j in sorted(x[i])[::-1]:
        #         ans+=[j]*i
        # return ans
        