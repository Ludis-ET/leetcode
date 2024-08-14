class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, max(nums)
        while l < r:
            m = l + ((r - l) // 2)
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > m and left <= right:
                    left += 1
                count += right - left
            if count < k:
                l = m + 1
            else:
                r = m
        return r

