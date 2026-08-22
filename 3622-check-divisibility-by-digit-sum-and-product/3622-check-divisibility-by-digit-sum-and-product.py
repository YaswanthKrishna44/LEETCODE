import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        org=n
        digits=[]
        while n>0:
            digit=n%10
            digits.append(digit)
            n=n//10
        if org%(sum(digits)+math.prod(digits))==0:
            return True 
        else:
            return False
        
        