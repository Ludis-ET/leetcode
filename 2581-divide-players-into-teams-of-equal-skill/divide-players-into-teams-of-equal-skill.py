class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        ans = 0
        last = skill[l] + skill[r]
        while l < r:
            n = skill[l] + skill[r]
            if last != n:
                return -1
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        return ans
