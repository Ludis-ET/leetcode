class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        l, r = 0, 0
        while r < len(chars):
            if chars[r] == chars[l]:
                r += 1
            else:
                ans.append(chars[l])
                if r - l > 1:
                    ans.extend(str(r - l))
                l = r
        ans.append(chars[l])
        if r - l > 1:
            ans.extend(str(r - l))
        chars[:len(ans)] = ans
        return len(ans)