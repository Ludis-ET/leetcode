class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        l, w = 0, 0
        for r in range(len(blocks)):
            if blocks[r] == 'W': w += 1

            if r - l + 1 > k:
                if blocks[l] == 'W': w -= 1
                l += 1
                
            if r - l + 1 == k:
                ans = min(ans, w)
        return ans if ans != float('inf') else 0
