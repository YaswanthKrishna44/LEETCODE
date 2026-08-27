class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[[]]
        for num in nums:
            new_subsets=[]
            for subset in result:
                new_set=subset+[num]
                if new_set not in result:
                    new_subsets.append(new_set)
            result.extend(new_subsets)
        return result


       
        