class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[[]]
        for num in nums:
            new_subset=[]
            for subset in result:
                new_subset.append(subset+[num])
            result.extend(new_subset)
        return result

        