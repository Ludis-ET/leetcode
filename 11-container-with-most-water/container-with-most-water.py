class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            length = min(height[r], height[l])
            width = r - l
            area = max(length * width, area)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return area
