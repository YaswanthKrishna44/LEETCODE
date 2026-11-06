class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # If we matched all characters in the word
            if i == len(word):
                return True
            
            # Check bounds, character match, and visited status (marked by '#')
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r, c - 1, i + 1))
            
            # Restore the cell (backtracking)
            board[r][c] = temp
            return found

        # Try starting the DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
        