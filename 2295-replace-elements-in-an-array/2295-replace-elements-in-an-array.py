class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            hashmap[num]=i
        for op in operations:
            x,y=op[:]
            hashmap[y]=hashmap[x]
            del hashmap[x]
            
        for k, i in hashmap.items():
            nums[i]=k
        return nums