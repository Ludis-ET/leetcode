class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex, ans = sorted(heights), 0
        for i, j in zip(heights, ex):
            ans += i != j
        return ans