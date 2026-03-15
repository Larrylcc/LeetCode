class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

    def rotate180(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
            matrix[i].reverse()
            matrix[n - i - 1].reverse()
        if n % 2 == 1:
            matrix[n // 2].reverse()

    def rotate270(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate_another_way(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] \
                    = matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate180(matrix)
    print(matrix)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate_another_way(matrix)
    print(matrix)
