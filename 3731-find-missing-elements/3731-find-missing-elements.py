class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set=set(nums)
        min_ele=min(nums)
        max_ele=max(nums)
        res=[]
        for i in range(min_ele,max_ele+1):
            if i not in nums_set:
                res.append(i)
        return res
        
        