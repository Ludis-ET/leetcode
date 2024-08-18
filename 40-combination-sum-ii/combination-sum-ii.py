class Solution:
    def combinationSum2(self, can: List[int], target: int) -> List[List[int]]:
        can.sort()
        ans = []
        def back(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i == len(can) or total > target: return
            cur.append(can[i])
            back(i + 1, cur, total + can[i])
            while i + 1 < len(can) and can[i] == can[i + 1]:
                i += 1
            cur.pop()
            back(i + 1, cur, total)
        back(0, [], 0)
        return ans