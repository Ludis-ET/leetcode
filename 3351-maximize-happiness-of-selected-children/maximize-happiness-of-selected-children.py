class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        n = ans = 0
        for i in happiness:
            if n >= k: break
            ans += max(0, i - n)
            n += 1
        return ans
