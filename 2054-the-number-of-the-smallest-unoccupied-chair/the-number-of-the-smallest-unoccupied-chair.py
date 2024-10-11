class Solution:
    def smallestChair(self, times: List[List[int]], target: int) -> int:
        for i, time in enumerate(times):
            times[i] = time + [i]
        chairs = []
        available = [i for i in range(len(times))]
        for a, l, i in sorted(times):
            while chairs and chairs[0][0] <= a:
                _, chair = heapq.heappop(chairs)
                heapq.heappush(available, chair)
            chair = heapq.heappop(available)
            heapq.heappush(chairs,(l, chair))
            if i == target: return chair