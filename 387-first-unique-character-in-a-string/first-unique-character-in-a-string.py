class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        for i, j in enumerate(s):
            if a[j] == 1:
                return i
        return -1
