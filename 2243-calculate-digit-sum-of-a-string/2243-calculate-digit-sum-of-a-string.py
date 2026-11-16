class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_str=[]
            for i in range(0,len(s),k):
                str_grp=s[i:i+k]
                tot_sum=sum(int(digit) for digit in str_grp)
                new_str.append(str(tot_sum))
            s= ''.join(new_str)
        return s
        