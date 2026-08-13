class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.dis(n-1,m-1,s,t,dp)
    def dis(self,i,j,s,t,dp):
        if j<0:
            return 1
        if i<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            dp[i][j]= self.dis(i-1,j-1,s,t,dp)+self.dis(i-1,j,s,t,dp)
        else:
            dp[i][j]=self.dis(i-1,j,s,t,dp)
        return dp[i][j]