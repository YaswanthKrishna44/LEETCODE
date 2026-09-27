class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for char in s:
            if char==')':
                rev=[]
                while stack and stack[-1]!='(':
                    rev.append(stack.pop())
                stack.pop()
                stack.extend(rev)
            else:
                stack.append(char)
        return  ''.join(stack)
        