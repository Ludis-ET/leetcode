class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        tmp = [-1] * len(nums) * 2
        stack = []
        nums += nums
        for i, j in enumerate(nums):
            while stack and stack[-1][0] < j:
                x, y = stack.pop()
                tmp[y] = j
            stack.append([j, i])

        return tmp[:len(nums) // 2]
        