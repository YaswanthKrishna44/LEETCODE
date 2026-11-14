class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counts=Counter(nums)
        res=[]
        for num,count in counts.items():
            if count> len(nums)//3:
                res.append(num)
        return res
        