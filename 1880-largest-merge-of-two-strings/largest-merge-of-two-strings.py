class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            if word1[l] > word2[r]:
                merge += word1[l]
                l += 1
            elif word1[l] == word2[r]:
                if word1[l:] > word2[r:]:
                    merge += word1[l]
                    l += 1
                else:
                    merge += word2[r]
                    r += 1
            else:
                merge += word2[r]
                r += 1
        return merge + word1[l:] + word2[r:]