class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        temp=[]
        temp.append(nums[0])
        for i in range(1,n):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                idx=self.bin_search(temp,nums[i])
                temp[idx]=nums[i]
        return len(temp)
    def bin_search(self,temp,target):
        left=0
        right=len(temp)-1
        while left<right:
            mid=left+(right-left)//2
            if temp[mid] < target:
                left = mid + 1
            else:
                right = mid 
        return left

        