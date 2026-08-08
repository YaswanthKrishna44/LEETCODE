class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if (total_sum+target)%2!=0 or total_sum<abs(target):
            return 0
        s1_target=(total_sum+target)//2
        
        # Shift values to handle negative integers if any
        dp = [[-1 for _ in range(s1_target + 1)] for _ in range(n + 1)]
        
       
        return self.subsetSum(n, s1_target, nums, dp)

    def subsetSum(self, n, target, nums, dp):
    
        if n == 0:
            return 1 if target==0 else 0
            
        if dp[n][target] != -1:
            return dp[n][target]
            
        not_taken = self.subsetSum(n - 1, target, nums, dp)
        taken = 0
        if nums[n - 1] <= target:
            taken = self.subsetSum(n - 1, target - nums[n - 1], nums, dp)
            
        dp[n][target] = taken+not_taken
        return dp[n][target]