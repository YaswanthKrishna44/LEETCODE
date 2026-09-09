class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        tot=0
        start=1000
        while start<=n:
            tot+=n-start+1
            start*=1000
        return tot
        