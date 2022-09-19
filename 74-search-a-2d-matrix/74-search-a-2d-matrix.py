class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        for i in range(row):
            if target in matrix[i]:
                return True