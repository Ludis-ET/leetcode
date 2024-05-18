class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        ans, cur = 0, 1
        l = 0
        for r in range(len(nums)):
            cur *= nums[r]
            while cur >= k:
                cur /= nums[l]
                l += 1
            ans += r -l + 1
        return ans