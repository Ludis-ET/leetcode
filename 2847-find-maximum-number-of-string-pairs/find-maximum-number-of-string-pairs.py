class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        nums, counter = {}, 0
        for a in words:
            if a[:] in nums or a[::-1] in nums:
                counter += 1
            else:
                nums[a] = 1
        return counter