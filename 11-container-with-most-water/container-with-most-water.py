class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height) - 1, 0
        while left < right:
            a, b = height[left], height[right]
            length = min(a, b)
            tmp = length * (right - left)
            area = max(tmp, area)
            if a < b:
                left += 1
            else:
                right -= 1
        return area

