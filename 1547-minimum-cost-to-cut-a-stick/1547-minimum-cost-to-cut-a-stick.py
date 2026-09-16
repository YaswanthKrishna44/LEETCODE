class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0,0)
        cuts.append(n)
        @cache
        def min_len(i,j):
            if i+1>=j:
                return 0
            min_cost=float('inf')
            for k in range(i+1,j):
                left=min_len(i,k)
                right=min_len(k,j)
                extra=cuts[j]-cuts[i]
                tot=left+right+extra
                min_cost=min(min_cost,tot)
            return min_cost
        return min_len(0,len(cuts)-1)

        