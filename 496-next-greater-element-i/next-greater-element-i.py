class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = {}
        stack = []
        for i, j in enumerate(nums2):
            while stack and stack[-1][0] < j:
                x, y = stack.pop()
                tmp[x] = j
            stack.append([j, i])
        ans = []
        for i in nums1:
            ans.append(tmp[i] if i in tmp else -1)
        return ans
