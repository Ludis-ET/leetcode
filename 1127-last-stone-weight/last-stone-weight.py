class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-k for k in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            f, s = heapq.heappop(stones), heapq.heappop(stones)
            if s > f:
                heapq.heappush(stones, f - s)
        stones.append(0)
        return abs(stones[0])