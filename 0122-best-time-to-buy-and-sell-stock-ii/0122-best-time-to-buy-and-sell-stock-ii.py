class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=-prices[0]
        not_hold=0
        for price in prices[1:]:
            hold=max(hold,not_hold-price)
            not_hold=max(not_hold,hold+price)
        return not_hold
        