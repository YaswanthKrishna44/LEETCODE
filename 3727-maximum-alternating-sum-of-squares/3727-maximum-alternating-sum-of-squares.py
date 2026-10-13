class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares=sorted(x*x for x in nums)
        n=len(squares)
        mid=n//2
        total_score = sum(squares[mid:]) - sum(squares[:mid])
        return total_score
        