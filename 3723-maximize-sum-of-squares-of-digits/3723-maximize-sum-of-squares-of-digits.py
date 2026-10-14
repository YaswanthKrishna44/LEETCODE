class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        # If the sum requires more than 9 per digit, it's impossible
        if s > n * 9:
            return ''
        
        # q is the number of '9's, r is the remaining sum for the next digit
        q, r = divmod(s, 9)
        
        # Build the prefix using maximum possible digits ('9's and the remainder)
        res = '9' * q + (str(r) if r else '')
        
        # Pad the remaining places with '0' to ensure length 'n'
        return res + '0' * (n - len(res))