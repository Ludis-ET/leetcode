class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        table = defaultdict(int)
        ans, count = 0, 0
        l = 0
        for r in range(len(fruits)):
            table[fruits[r]] += 1
            count += 1
            while len(table) > 2:
                table[fruits[l]] -= 1
                count -= 1
                if table[fruits[l]] == 0:
                    del table[fruits[l]]
                l += 1
            ans = max(ans, count)
        return ans
