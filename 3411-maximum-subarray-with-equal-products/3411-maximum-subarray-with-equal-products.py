import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len=2
        curr_prod=1
        left=0
        for right in range(len(nums)):
            while math.gcd(curr_prod,nums[right])>1:
                curr_prod//=nums[left]
                left+=1
            curr_prod *= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len
            
        