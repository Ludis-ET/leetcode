class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set1 = set(allowed)
        res = 0
        for w in words:
            if set(w).issubset(set1):
                res += 1
        return res


            