class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = []
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l += 1
                r += 1
            else:
                s = prices[r] - prices[l]
                if s > 0:
                    ans.append(s)
                l = r
                r += 1
        return sum(ans)