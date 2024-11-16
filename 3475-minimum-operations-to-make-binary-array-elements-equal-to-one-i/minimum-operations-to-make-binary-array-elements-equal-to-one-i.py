class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans, z = 0, 0
        for r in range(len(nums)):
            z += not nums[r]
            if r > 1:
                l = r - 2
                if not nums[l]:
                    ans += 1
                    nums[l] = not nums[l]
                    z -= 1
                    z = z + 1 if nums[l + 1] else z - 1
                    z = z + 1 if nums[l + 2] else z - 1
                    nums[l + 1] = not nums[l + 1]
                    nums[l + 2] = not nums[l + 2]
        return ans if not z else -1
