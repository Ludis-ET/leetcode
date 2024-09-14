class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        tmp = [-i for i in Counter(arr).values()]
        heapq.heapify(tmp)
        n = (len(arr) // 2) + (len(arr) % 2)
        x = 0
        while n > 0:
            n += heapq.heappop(tmp)
            x += 1
        return x