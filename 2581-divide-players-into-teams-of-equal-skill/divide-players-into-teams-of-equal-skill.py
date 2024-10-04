class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        div = sum(skill) / (n/2)
        arr = []
        l, r = 0, n - 1

        while l < r:
            if skill[l] + skill[r] == div:
                arr.append([skill[l], skill[r]])
                l += 1
                r -= 1
            elif skill[l] + skill[r] < div:
                l += 1
            else:    
                r -= 1
        res = 0
        for i, j in arr:
            res += (i * j)
        if len(arr) != n/2:
            return -1
        return res if res else -1

            
        
        