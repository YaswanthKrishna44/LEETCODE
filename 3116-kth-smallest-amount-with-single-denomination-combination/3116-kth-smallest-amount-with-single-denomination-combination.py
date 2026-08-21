class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_less(target):
            count=0
            n=len(coins)
            for size in range(1,n+1):
                for comb in combinations(coins,size):
                    lcm=math.lcm(*comb)
                    multiples=target//lcm
                    if size%2==1:
                        count+=multiples
                    else:
                        count-=multiples
            return count
        low=1
        high=min(coins)*k
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            if count_less(mid)>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        

        