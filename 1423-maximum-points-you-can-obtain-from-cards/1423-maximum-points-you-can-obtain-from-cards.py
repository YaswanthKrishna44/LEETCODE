class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        if k<0 or k>n:
            return -1
        if k==0:
            return 0
        if k==n:
            return sum(cardPoints)
        curr_score=sum(cardPoints[:k])
        max_score=curr_score
        right_index=n-1
        for left_index in range(k-1,-1,-1):
            curr_score-=cardPoints[left_index]
            curr_score+=cardPoints[right_index]
            right_index-=1
            if curr_score>max_score:
                max_score=curr_score
        return max_score

        