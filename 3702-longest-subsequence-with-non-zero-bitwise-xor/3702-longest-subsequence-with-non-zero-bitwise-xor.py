class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if not any(nums):
            return 0
        #maxlen=0
        res=0
        for i in range(0,len(nums)):
            res=res^nums[i]
        if res!=0:
            return len(nums)
                
        return len(nums)-1