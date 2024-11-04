class Solution:
    def compressedString(self, word: str) -> str:
        ans, i = "", 0
        while i < len(word):
            c, comp = 1, word[i]
            i += 1
            while i < len(word) and c < 9 and word[i] == comp:
                c += 1
                i += 1
            ans += str(c) + comp
        return ans