class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max=nums[0]
        curr_min=nums[0]
        ans=nums[0]
        for x in nums[1:]:
            candidates=(x,curr_max*x,curr_min*x)
            curr_max=max(candidates)
            curr_min=min(candidates)
            ans=max(ans,curr_max)
        return ans 
        