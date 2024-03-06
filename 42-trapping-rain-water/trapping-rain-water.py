class Solution:
    def trap(self, height: List[int]) -> int:
        first, last = 0, len(height) - 1
        leftMx , rightMx = height[first], height[last]
        ans = 0
        while first < last:
            if leftMx < rightMx:
                first += 1
                leftMx = max(leftMx,height[first])
                ans += leftMx - height[first]
            else:
                last -= 1
                rightMx = max(rightMx,height[last])
                ans += rightMx - height[last]
        return ans