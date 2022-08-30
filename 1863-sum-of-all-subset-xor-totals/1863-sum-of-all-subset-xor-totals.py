class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import chain, combinations
        def xor_of_arr(arr):
            ans = 0
            for i in arr:
                ans = ans ^ i
            return ans
        
        def powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
        
        ans = 0
        
        for i in powerset(nums):
            ans += xor_of_arr(i)
            
        return ans