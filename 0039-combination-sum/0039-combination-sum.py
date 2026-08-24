class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dice(p, nums, target, start):
            if target == 0:
                return [p]
            res = []
            for i in range(start, len(nums)):
                num = nums[i]
                if num <= target:
                    res += dice(p + [num], nums, target - num, i)  # i, not 0, to avoid reordering
            return res
        return dice([], candidates, target, 0)
        