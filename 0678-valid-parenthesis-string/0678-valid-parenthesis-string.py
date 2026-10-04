class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []      # Stores indices of '('
        star_stack = [] # Stores indices of '*'
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                star_stack.append(i)
            else:  # ch == ')'
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        # Match remaining '(' with '*' that appear after them
        while stack and star_stack:
            if stack[-1] < star_stack[-1]:
                stack.pop()
                star_stack.pop()
            else:
                return False
                
        return len(stack) == 0