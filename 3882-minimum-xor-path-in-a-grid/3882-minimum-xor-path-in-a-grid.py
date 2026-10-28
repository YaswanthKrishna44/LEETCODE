class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp = [[None] * m for _ in range(n)]
        return min(self.func(n-1,m-1,grid,dp))
    def func(self,i,j,grid,dp):
        if i==0 and j==0:
            return {grid[0][0]}
        if i<0 or j<0:
            return set()
        if dp[i][j] is not None:
            return dp[i][j]
        res=set()
        for x in self.func(i-1,j,grid,dp):
            res.add(grid[i][j]^x)
        for x in self.func(i,j-1,grid,dp):
            res.add(grid[i][j]^x)
        dp[i][j]=res
        return dp[i][j]
        