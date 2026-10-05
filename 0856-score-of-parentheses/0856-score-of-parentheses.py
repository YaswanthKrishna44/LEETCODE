class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=[0]
        for parentheses in s:
            if parentheses=='(':
                score.append(0)
            elif score:
                last_score=score.pop()
                score[-1]+=max(1,last_score*2)
        return score[-1]
        