class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        
        stable_ind=float('inf')
        for i in range(len(nums)):
            inst_score=max(nums[0:i+1])-min(nums[i:len(nums)+1])
            if inst_score<=k:
                stable_ind=min(stable_ind,i)
        
        return stable_ind if stable_ind!=float('inf') else -1

        