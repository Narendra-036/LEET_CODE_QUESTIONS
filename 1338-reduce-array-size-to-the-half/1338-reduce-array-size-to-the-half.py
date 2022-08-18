class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        
        check = [0]*(n+1)
        for c in Counter(arr).values():
            check[c] += 1
        
        half = len(arr) // 2
        
        ans = 0
        count = 0

        for i in range(n, -1, -1):
            
            while check[i]:
                ans += 1
                count += i
                
                if count >= half:
                    return ans
                
                check[i] -= 1
        
        return ans