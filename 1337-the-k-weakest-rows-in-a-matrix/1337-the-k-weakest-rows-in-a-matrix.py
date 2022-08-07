class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row = []
        for i in range(len(mat)):
            row.append((sum(mat[i]), i))
        print(row)
        row.sort()
        ans = [idx for (val, idx) in row[:k]]

        return ans