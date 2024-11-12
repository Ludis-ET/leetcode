class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([[j, i] for i, j in enumerate(queries)])
        res, tmp = [], []
        mx, l = 0, 0
        for q, i in queries:
            while l < len(items) and q >= items[l][0]:
                mx = max(mx, items[l][1])
                l += 1
            heapq.heappush(tmp, [i, mx])
        while tmp:
            res.append(heapq.heappop(tmp)[1])
        return res