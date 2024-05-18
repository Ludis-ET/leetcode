class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[i] + cardPoints[i])
        ans = 0
        l, r = k - 1, n
        while (l + 1) != -1:
            ans = max(ans, (prefix[l + 1]) + (prefix[n] - prefix[r]))
            l -= 1
            r -= 1
        return ans

                