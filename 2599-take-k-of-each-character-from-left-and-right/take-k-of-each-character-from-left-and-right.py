class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        table = Counter(s)

        def check():
            for i in ['a', 'b', 'c']:
                if table[i] < k:
                    return False
            return True

        if not check(): return -1
        l = 0
        ans = float('inf')
        for r in range(len(s)):
            table[s[r]] -= 1
            while not check():
                table[s[l]] += 1
                l += 1
            ans = min(ans, len(s) - (r - l + 1))
        return ans