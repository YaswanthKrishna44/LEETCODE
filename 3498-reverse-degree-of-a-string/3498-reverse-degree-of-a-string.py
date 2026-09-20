class Solution:
    def reverseDegree(self, s: str) -> int:
        prods=[]
        for i in range(0,len(s)):
            reversed_ind= 26 - (ord(s[i]) - ord('a'))
            ind_s=i+1
            prods.append(reversed_ind*ind_s)
        return sum(prods)


        