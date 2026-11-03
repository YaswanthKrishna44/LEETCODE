class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val=min(nums)
        return sum(abs(min_val-num) for num in nums)
        