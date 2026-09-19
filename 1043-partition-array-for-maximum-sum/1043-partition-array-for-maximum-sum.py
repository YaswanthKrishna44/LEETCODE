class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n=len(arr)
        dp=[-1]*n
        return self.fun(0,arr,k,dp)
    def fun(self,ind,arr,k,dp):
        n=len(arr)
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        leng=0
        maxi=float('-inf')
        maxans=float('-inf')
        for j in range(ind,min(ind+k,n)):
            leng+=1
            maxi=max(maxi,arr[j])
            sum=leng*maxi+self.fun(j+1,arr,k,dp)
            maxans=max(maxans,sum)
        dp[ind]=maxans
        return dp[ind]
        
        