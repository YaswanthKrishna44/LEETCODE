class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(0,n-2):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,n-1
            while left<right:
                tot_sum=nums[i]+nums[left]+nums[right]
                if tot_sum<0:
                    left+=1
                elif tot_sum>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return res
        