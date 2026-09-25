class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[float('inf')] * m for _ in range(n)]
        # Check all possible starting columns in the bottom row
        return min(self.func(n - 1, j, matrix, dp) for j in range(m))
    def func(self, i, j, matrix, dp):
        # Base case: reached the top row
        # Out of bounds check for columns
        if j < 0 or j >= len(matrix[0]):
            return float('inf')
        if i == 0:
            return matrix[0][j]  
        if dp[i][j] != float('inf'):
            return dp[i][j]   
        up = matrix[i][j] + self.func(i - 1, j, matrix, dp)
        left = matrix[i][j] + self.func(i - 1, j - 1, matrix, dp)   # top-left diagonal
        right = matrix[i][j] + self.func(i - 1, j + 1, matrix, dp)  # top-right diagonal
        dp[i][j] = min(up, left, right)
        return dp[i][j]