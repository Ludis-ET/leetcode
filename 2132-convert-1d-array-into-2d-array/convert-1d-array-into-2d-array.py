class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original): return []
        ans, i = [], 0
        while i < len(original):
            tmp, count = [], n
            while i < len(original) and count > 0:
                tmp.append(original[i])
                count -= 1
                i += 1
            ans.append(tmp)
        return ans