class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        left=0
        curr_sum=0
        min_lens=[float('inf')]*n
        best=float('inf')
        curr_min=float('inf')
        for right in range(n):
            curr_sum+=arr[right]
            while curr_sum>target and left<=right:
                curr_sum-=arr[left]
                left+=1
            if curr_sum==target:
                leng=right-left+1
                if left>0 and min_lens[left-1]!=float('inf'):
                    best=min(best,leng+min_lens[left-1])
                curr_min=min(curr_min,leng)
            min_lens[right]=curr_min
        return best if best!=float('inf') else -1



        