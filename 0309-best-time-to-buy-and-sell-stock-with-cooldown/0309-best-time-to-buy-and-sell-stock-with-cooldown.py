class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold=-prices[0]
        sold=0
        rest=0
        for price in prices[1:]:
            prev_hold=hold
            prev_sold=sold
            hold=max(prev_hold,rest-price)
            sold=prev_hold+price
            rest=max(rest,prev_sold)
        return max(sold,rest)
        