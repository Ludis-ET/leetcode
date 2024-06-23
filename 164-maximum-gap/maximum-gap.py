class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, abs(nums[i] - nums[i + 1]))
        return ans if len(nums) >= 2 else 0