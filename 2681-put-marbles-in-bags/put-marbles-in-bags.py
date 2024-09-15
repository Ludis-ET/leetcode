class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        mx, mn = [], []
        for i in range(1, len(weights)):
            heapq.heappush(mn, weights[i] + weights[i - 1])
            heapq.heappush(mx, -(weights[i] + weights[i - 1]))
        ans = 0
        for _ in range(k - 1):
            ans += -heapq.heappop(mx)

        for _ in range(k - 1):
            ans -= heapq.heappop(mn)

        return ans        