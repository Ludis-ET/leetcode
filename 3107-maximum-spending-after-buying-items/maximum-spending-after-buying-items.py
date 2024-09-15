class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = []
        for i in values:
            for j in i:
                heapq.heappush(heap, j)
        ans, d = 0, 1
        while heap:
            ans += (heapq.heappop(heap) * d)
            d += 1
        return ans