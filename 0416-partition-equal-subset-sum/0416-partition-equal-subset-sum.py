class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it cannot be partitioned into two equal integer subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # dp stores achievable subset sums represented as a bitmask/set
        dp = 1  # Base case: sum of 0 is always achievable (1 << 0)
        
        for num in nums:
            # Shift bits by `num` to mark all new reachable sums, then bitwise-OR with existing
            dp |= dp << num
            
            # Early exit if target bit is set
            if (dp >> target) & 1:
                return True
                
        return bool((dp >> target) & 1)
        