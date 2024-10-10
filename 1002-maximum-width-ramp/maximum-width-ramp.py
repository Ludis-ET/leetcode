class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxes = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            maxes[i] = nums[i] if nums[i] > maxes[i + 1] else maxes[i + 1]
        ans = 0
        l, r = 0, 1
        while r < len(nums):
            if nums[l] <= maxes[r]:
                ans = max(ans, r - l)
                r += 1
            else:
                l += 1
        return ans