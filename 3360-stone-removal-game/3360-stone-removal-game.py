class Solution:
    def canAliceWin(self, n: int) -> bool:
        st_rem=10
        turns=0
        while n>=st_rem:
            n-=st_rem
            st_rem-=1
            turns+=1
        return turns%2==1