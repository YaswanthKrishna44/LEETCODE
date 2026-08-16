class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[-1]*(m+1) for _ in range(n)]
        return self.wildmatching(s, p, n - 1, m - 1, dp)
    def isAllStars(self, p, i):
        for j in range(i + 1):
            if p[j] != '*':
                return False
        return True
    def wildmatching(self,s,p,i,j,dp):
        if i<0 and j<0:
            return True
        if i<0 and j>=0:
            return  self.isAllStars(p, j)
        if j<0 and i>=0:
            return False
        if dp[i][j]!=-1:
            return dp[i][j]==1
        elif s[i]==p[j] or p[j]=='?' :
            dp[i][j]=1 if self.wildmatching(s,p,i-1,j-1,dp) else 0
        elif p[j]=='*':
            dp[i][j]= 1 if (self.wildmatching(s, p, i - 1, j, dp) or
                              self.wildmatching(s, p, i, j - 1, dp)) else 0
        else:
            dp[i][j]=0
        return dp[i][j]==1

        