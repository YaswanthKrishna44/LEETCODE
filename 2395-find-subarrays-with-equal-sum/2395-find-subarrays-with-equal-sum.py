class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n=len(nums)
        seen_sum=set()
        for i in range(0,n-1):
            curr_sum=nums[i]+nums[i+1]
            if curr_sum in seen_sum:
                return True
            seen_sum.add(curr_sum)
        return False
        