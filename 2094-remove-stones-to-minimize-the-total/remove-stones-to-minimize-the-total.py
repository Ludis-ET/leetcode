class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-k for k in piles]
        heapq.heapify(piles)
        for _ in range(k):
            top = abs(heapq.heappop(piles))
            heapq.heappush(piles, -(top - (top // 2)))
        return sum(abs(k) for k in piles)