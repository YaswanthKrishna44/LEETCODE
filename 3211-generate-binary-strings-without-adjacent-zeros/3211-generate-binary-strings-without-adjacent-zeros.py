class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n==0:
            return ['']
        if n==1:
            return ['0','1']
        result=[]
        for s in self.validStrings(n-1):
            result.append(s+'1')
        for s in self.validStrings(n-2):
            result.append(s+'10')
        return sorted(result)

        