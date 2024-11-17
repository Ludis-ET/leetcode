class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans, pre = float('inf'), 0
        q = deque()
        for r, num in enumerate(nums):
            pre += num
            if pre >= k:
                ans = min(ans, r + 1)

            while q and pre - q[0][0] >= k:
                ans = min(ans, r - q.popleft()[1])

            while q and q[-1][0] > pre:
                q.pop()
            q.append((pre, r))
        return -1 if ans == float('inf') else ans