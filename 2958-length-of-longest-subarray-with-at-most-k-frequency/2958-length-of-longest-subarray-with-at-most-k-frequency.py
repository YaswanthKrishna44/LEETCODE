class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        maxCount=0
        i=0
        for j in range(len(nums)):
            freq[nums[j]]=freq.get(nums[j],0)+1
            while freq[nums[j]]>k:
                freq[nums[i]]-=1
                i+=1
            maxCount=max(maxCount,j-i+1)
        return maxCount
        
        