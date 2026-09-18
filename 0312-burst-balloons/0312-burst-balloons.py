class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n=len(nums)
        arr=[1]+nums+[1]
        dp=[[-1]*(n+2) for _ in range(n+2)]
        #return balloon(arr,1,n)
        def balloon(arr,i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for k in range(i,j+1):
                cost=arr[i-1]*arr[k]*arr[j+1]+balloon(arr,i,k-1)+balloon(arr,k+1,j)
                maxi=max(maxi,cost)
            dp[i][j]=maxi
            return maxi
        return balloon(arr,1,n)
        

        