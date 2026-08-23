class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        l_sum=r_sum=0
        q_l=q_r=0
        for i in range(n//2):
            if num[i]=='?':
                q_l+=1
            else:
                l_sum+=int(num[i])
            if num[n//2+i]=='?':
                q_r+=1
            else:
                r_sum+=int(num[n//2+i])
        if (q_l+q_r)%2!=0:
            return True
        return 2*(l_sum-r_sum)!=9*(q_r-q_l)
        