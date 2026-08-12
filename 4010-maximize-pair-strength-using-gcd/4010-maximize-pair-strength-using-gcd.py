import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        max_val = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                val = (nums[i] * nums[j]) // (math.gcd(nums[i], nums[j]) ** 2)
                if val > max_val:
                    max_val = val
        return max_val