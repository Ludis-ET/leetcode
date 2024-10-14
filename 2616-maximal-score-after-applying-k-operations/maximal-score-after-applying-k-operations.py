class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            heapq.heappush(hp, -num)
        ans = 0
        for _ in range(k):
            num = -heapq.heappop(hp)
            ans += num
            heapq.heappush(hp, -ceil(num / 3))
        return ans