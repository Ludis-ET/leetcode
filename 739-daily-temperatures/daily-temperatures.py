class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and stack[-1][0] < j:
                x, y = stack.pop()
                ans[y] = i - y
            stack.append([j,i])
        return ans

            