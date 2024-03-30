class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for a in range(max(len(word1),len(word2))):
            if a < len(word1):
                ans += word1[a]
            if a < len(word2):
                ans += word2[a]
        return ans

    

        



         