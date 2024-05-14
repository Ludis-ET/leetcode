class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, ans, cur = 0, float('-inf'), 0
        for r in range(len(nums)):
            cur += nums[r]
            if r - l + 1 == k:
                ans = max(cur, ans)
                cur -= nums[l]
                l += 1
        return ans / k

