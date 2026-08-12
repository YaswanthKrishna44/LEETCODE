class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        totsum=0.0
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        for i in range(min(len(prices),len(discounts))):
            dis_price=prices[i]*(100-discounts[i])/100
            totsum+=dis_price
        for i in range(min(len(prices),len(discounts)),len(prices)):
            totsum+=prices[i]
        return totsum
