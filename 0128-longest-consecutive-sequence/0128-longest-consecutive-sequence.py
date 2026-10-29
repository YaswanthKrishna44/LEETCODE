class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_count=1
        count=1
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==curr+1:
                count+=1
                curr=nums[i]
            else:
                max_count=max(max_count,count)
                curr=nums[i]
                count=1
        return max(max_count,count)