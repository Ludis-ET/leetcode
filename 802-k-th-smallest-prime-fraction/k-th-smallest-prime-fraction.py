class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heapq.heappush(heap, [arr[i]/arr[j], i, j])
        for _ in range(k - 1): heapq.heappop(heap)
        return [arr[heap[0][1]], arr[heap[0][2]]]