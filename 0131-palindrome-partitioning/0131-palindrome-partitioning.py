class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [-1] * (n + 1)
        return self.func(0, n, s, dp)

    def func(self, i, n, s, dp):
        if i == n:
            return [[]]  # Base case: 1 valid partition consisting of empty parts
        if dp[i] != -1:
            return dp[i]

        all_partitions = []
        for j in range(i, n):
            if self.isPalindrome(i, j, s):
                current_palindrome = s[i : j + 1]
                # Get all valid partitionings for the remainder of the string
                sub_partitions = self.func(j + 1, n, s, dp)
                
                # Append current palindrome to the beginning of each sub-partition
                for part in sub_partitions:
                    all_partitions.append([current_palindrome] + part)

        dp[i] = all_partitions
        return dp[i]

    def isPalindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        