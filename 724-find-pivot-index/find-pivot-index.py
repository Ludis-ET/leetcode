class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x, y = sum(nums), 0
        
        for i in range(len(nums)):
            if y == x - (y + nums[i]):
                return i
            y += nums[i]
        return -1