class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cur = 1 + nums[0]
        for i in range(1, len(nums)):
            if cur > nums[i]:
                ans += cur - nums[i]
                cur += 1 
            else:
                cur = 1 + nums[i]
        return ans