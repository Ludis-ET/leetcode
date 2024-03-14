class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        ans = ""
        for b in range(len(first)):
            for a in range(1, len(strs)):
                if b >= len(strs[a]) or strs[a][b] != first[b]:
                    return ans
            ans += first[b]
        return ans