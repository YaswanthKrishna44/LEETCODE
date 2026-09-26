class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]
        return self.func(n-1,m-1,grid,dp)
    def func(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=float('inf'):
            return dp[i][j]
        up=grid[i][j]+self.func(i-1,j,grid,dp)
        left=grid[i][j]+self.func(i,j-1,grid,dp)
        dp[i][j]=min(up,left)
        return dp[i][j]