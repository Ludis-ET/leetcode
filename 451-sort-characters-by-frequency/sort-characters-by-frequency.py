class Solution:
    def frequencySort(self, s: str) -> str:
        heap = [[-j, i] for i, j in Counter(s).items()]
        heapq.heapify(heap)
        ans = ""
        while heap:
            tmp = heapq.heappop(heap)
            ans += (tmp[1] * -tmp[0])
        return ans