class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ""
        for i in s: convert += str(ord(i) - ord('a') + 1)
        for _ in range(k):
            new = 0
            for i in convert: new += int(i)
            convert = str(new)
        return int(convert)