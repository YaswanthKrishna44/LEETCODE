class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples = [k * i for i in range(1, len(nums) + 2)]
        for multiple in multiples:
            if multiple in nums:
                continue
            else:
                return multiple