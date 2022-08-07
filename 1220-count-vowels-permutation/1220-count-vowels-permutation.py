class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD =  pow(10,9) + 7
        def multiply(a, b):
            
            result = [ [0] * len(b[0]) for _ in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b[0])):
                    for k in range(len(a[0])):
                        result[i][j] += (a[i][k] * b[k][j]) % MOD
                        result[i][j] %= MOD
            return result
        
        
        adjacency_matrix = [
            [0,1,0,0,0],
            [1,0,1,0,0],
            [1,1,0,1,1],
            [0,0,1,0,1],
            [1,0,0,0,0]
        ]
        
        result = [[0]*5 for _ in range(5)]
        for i in range(5):
            result[i][i] = 1
        
        s = 0
        n -= 1
        while n:
            if n & 1:
                result = multiply(adjacency_matrix,result)
            n >>= 1
            adjacency_matrix = multiply(adjacency_matrix,adjacency_matrix)
        
        for i in range(5):
            s += sum(result[i])
        
        return s % MOD 