class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        prev = ""
        for i in s:
            prev += i
            while len(prev) >= len(part) and prev[len(prev) - len(part):] == part:
                prev = prev[:len(prev) - len(part)]
        return prev