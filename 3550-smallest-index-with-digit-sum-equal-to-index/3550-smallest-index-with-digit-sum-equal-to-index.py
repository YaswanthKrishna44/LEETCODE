class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            digit_sum = sum(map(int, str(num)))
            if i==digit_sum:
                return i
        return -1
        