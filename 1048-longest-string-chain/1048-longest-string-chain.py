class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # Sort words by length so we process shorter words first
        words.sort(key=len)
        
        # dp stores the maximum chain length ending at each word
        dp = {}
        max_chain = 1
        
        for word in words:
            current_max = 1
            # Generate all possible predecessors by removing one letter
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    current_max = max(current_max, dp[predecessor] + 1)
            
            dp[word] = current_max
            max_chain = max(max_chain, current_max)
            
        return max_chain
        