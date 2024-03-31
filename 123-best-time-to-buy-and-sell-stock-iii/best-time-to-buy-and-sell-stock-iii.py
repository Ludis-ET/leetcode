class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        x = y = float('inf')
        l = r = 0

        for price in prices:
            x = min(x, price)
            l = max(l, price - x)

            y = min(y, price - l)
            r = max(r, price - y)

        return r