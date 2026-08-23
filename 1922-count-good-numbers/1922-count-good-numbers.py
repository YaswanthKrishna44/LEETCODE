class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even_indices = (n + 1) // 2
        odd_indices = n // 2
        
        # pow(base, exp, mod) computes (base^exp) % mod in O(log exp) time
        return (pow(5, even_indices, MOD) * pow(4, odd_indices, MOD)) % MOD
        