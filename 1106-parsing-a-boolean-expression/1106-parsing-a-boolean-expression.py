class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ',':
                continue
            elif char != ')':
                stack.append(char)
            else:
                # Gather all values inside the current parentheses
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                
                # Remove the '('
                stack.pop()
                
                # Get the operator before '('
                op = stack.pop()
                
                # Evaluate based on operator
                if op == '!':
                    stack.append('f' if 't' in seen else 't')
                elif op == '&':
                    stack.append('f' if 'f' in seen else 't')
                elif op == '|':
                    stack.append('t' if 't' in seen else 'f')
                    
        return stack[-1] == 't'