class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                s = prices[r] - prices[l]
                profit = max(profit, s)
                r += 1
        return profit