class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # If start or destination is an obstacle, there are no valid paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0 
        dp = [[-1] * n for _ in range(m)]
        return self.func(m - 1, n - 1, obstacleGrid, dp)
    def func(self, i, j, obstacleGrid, dp):
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        up = self.func(i - 1, j, obstacleGrid, dp)
        left = self.func(i, j - 1, obstacleGrid, dp)
        dp[i][j] = up + left
        return dp[i][j]
        