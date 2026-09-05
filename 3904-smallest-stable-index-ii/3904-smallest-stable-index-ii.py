class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if len(nums)==1:
            return 0
        min_suf=[0]*len(nums)
        min_suf[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            min_suf[i]=min(nums[i],min_suf[i+1])
        max_pref=float('-inf')
        for i in range(n):
            max_pref=max(max_pref,nums[i])
            inst_score=max_pref-min_suf[i]
            if inst_score<=k:
                return i
        return -1

        
        