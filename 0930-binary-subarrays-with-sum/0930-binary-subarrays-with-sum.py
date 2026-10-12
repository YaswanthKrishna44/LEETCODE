class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            left=0
            #right=0
            count=0
            curr_sum=0
            for right in range(len(nums)):
                curr_sum+=nums[right]
                while curr_sum>k:
                    curr_sum-=nums[left]
                    left+=1
                count+=right-left+1
            return count
        return atmost(goal) - atmost(goal - 1)
