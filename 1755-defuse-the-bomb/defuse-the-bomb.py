class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)
        code += code
        neg = k < 0
        cur, k = 0, abs(k)
        l = (len(code) // 2) - k if neg else 0
        ans = []
        for r in range((len(code) // 2) - k if neg else 0, len(code)):
            cur += code[r]
            if r - l + 1 == k + 1:
                if neg:
                    ans.append(cur - code[r])
                    cur -= code[l]
                else:
                    cur -= code[l]
                    ans.append(cur)
                l += 1
        return ans[:len(code) // 2]