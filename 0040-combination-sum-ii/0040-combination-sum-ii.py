class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        def dice(p, nums, target):
            if target == 0:
                return [p]
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                num = nums[i]
                if num <= target:
                    res += dice(p + [num], nums[i+1:], target - num)  # i, not 0, to avoid reordering
            return res
        return dice([], candidates, target)
        