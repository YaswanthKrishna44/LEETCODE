class Solution:
    def maxProduct(self, n: int) -> int:
        res=[]
        for s in str(n):
            res.append(int(s))
        l=len(res)
        res.sort()
        return res[l-2]*res[l-1]

        