class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, n - 1
        while i < m and 0 <= j:
            temp = matrix[i][j]
            if temp > target:
                j -= 1
            elif temp < target:
                i += 1
            else:
                return True
        return False
