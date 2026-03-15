class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = []
        i, j, dir = 0, 0, 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x = i + dirs[dir][0]
            y = j + dirs[dir][1]
            if matrix[x][y] is None or x < 0 or x >= m or y < 0 or y >= n:
                dir = (dir + 1) % 4
            i += dirs[dir][0]
            j += dirs[dir][1]
        return ans
