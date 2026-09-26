class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        return self.func(0,0,m-1,n,m,grid,dp)
    def func(self,i,j1,j2,n,m,grid,dp):
        if (j1<0 or j2<0 or j1>=m or j2>=m):
            return -1
        if i==n-1:
            if j1==j2:
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        maxi=-1
        for dj1 in range(-1,2):
            for dj2 in range(-1,2):
                val=0
                if j1==j2:
                    val=grid[i][j1]
                else:
                    val=grid[i][j1]+grid[i][j2]
                val+=self.func(i+1,j1+dj1,j2+dj2,n,m,grid,dp)
                maxi=max(maxi,val)
        dp[i][j1][j2] = maxi
        return maxi

        