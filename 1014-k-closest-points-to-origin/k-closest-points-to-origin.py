class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans, heap = [], []
        for i, j in points:
            d = pow(i, 2) + pow(j, 2)
            heap.append([d, i, j])
        heapq.heapify(heap)
        while k > 0:
            _, i, j = heapq.heappop(heap)
            ans.append([i, j])
            k -= 1
        return ans