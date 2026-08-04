class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        n=len(arr)
        totsum=sum(arr)
        if totsum%2!=0:
            return False
        k=totsum//2
        dp=[[-1]*(k+1) for _ in range(n)]
        return self.eqpartition(n-1,k,arr,dp)
    def eqpartition(self,ind,target,arr,dp):
        if target==0:
            return True
        if ind==0:
            return arr[0]==target
        if dp[ind][target]!=-1:
            return dp[ind][target]==1
        not_taken=self.eqpartition(ind-1,target,arr,dp)
        taken=False
        if arr[ind]<=target:
            taken=self.eqpartition(ind-1,target-arr[ind],arr,dp)
        dp[ind][target]=1 if (taken or not_taken) else 0
        return taken or not_taken

        