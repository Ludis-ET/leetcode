class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        large, small = [], [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(small)
        for _ in range(k):
            while small and small[0][0] <= w:
                heapq.heappush(large, -(heapq.heappop(small)[1]))
            if large:
                w += -heapq.heappop(large)
        return w
