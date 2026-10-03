class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if not nums or k <= 0 or k > len(nums):
            return 0
        freq={}
        for x in nums[:k]:
            freq[x]=freq.get(x,0)+1
        curr_sum=sum(nums[:k])
        max_sum=curr_sum if len(freq)==k else 0
        for i in range(k,len(nums)):
            curr_sum+=nums[i]-nums[i-k]
            freq[nums[i]]=freq.get(nums[i],0)+1
            freq[nums[i-k]]-=1
            if freq[nums[i-k]]==0:
                del freq[nums[i-k]]
            if len(freq)==k:
                max_sum=max(max_sum,curr_sum)
        return max_sum