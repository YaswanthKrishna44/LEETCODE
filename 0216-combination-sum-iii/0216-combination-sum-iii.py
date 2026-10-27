class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res=[]
        def recur(st,curr_comb,curr_sum):
            if len(curr_comb)==k:
                if curr_sum==n:
                    res.append(list(curr_comb))
                return
            if curr_sum>n:
                return
            for i in range(st,10):
                curr_comb.append(i)
                recur(i+1,curr_comb,curr_sum+i)
                curr_comb.pop()
        recur(1,[],0)
        return res
        