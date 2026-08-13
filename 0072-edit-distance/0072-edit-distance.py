class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.editDistanceUtil(word1,word2,n-1,m-1,dp)
    def editDistanceUtil(self,word1,word2,i,j,dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

    # If the result for this subproblem is already computed, return it
        if dp[i][j] != -1:
            return dp[i][j]

    # If the characters at the current positions match, no operation is needed
        if word1[i] == word2[j]:
            dp[i][j] = self.editDistanceUtil(word1, word2, i - 1, j - 1, dp)
        else:
        # Calculate the minimum of three choices:
        # 1. Replace the current character (diagonal move)
        # 2. Insert a character into S1 (move up)
        # 3. Delete a character from S1 (move left)
            dp[i][j] = 1 + min(self.editDistanceUtil(word1, word2, i - 1, j - 1, dp),min(self.editDistanceUtil(word1, word2, i - 1, j, dp), self.editDistanceUtil(word1, word2, i, j - 1, dp))
        )

        return dp[i][j]

        