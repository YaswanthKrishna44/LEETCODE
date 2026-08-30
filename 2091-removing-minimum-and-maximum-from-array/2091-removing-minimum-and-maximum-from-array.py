class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        i=min(min_idx,max_idx)
        j=max(min_idx,max_idx)
        both_front=j+1
        both_back=n-i
        from_both_ends=(i+1)+(n-j)
        return min(both_front,both_back,from_both_ends)
        