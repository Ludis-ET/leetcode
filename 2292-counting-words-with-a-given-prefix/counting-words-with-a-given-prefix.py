class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for a in words:
            if len(a) >= len(pref) and a[:len(pref)] == pref:
                count += 1
        return count
        