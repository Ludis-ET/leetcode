class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = nums[0], 0
        for num in nums:
            cur = cur + num if cur > 0 else num
            ans = max(ans, cur)
        return ans