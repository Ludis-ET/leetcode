class Solution:
    def findLHS(self, nums: List[int]) -> int:
        table = defaultdict(int)

        for i in nums:
            table[i] += 1
        
        ans = float('-inf')
        for i in table.keys():
            if i + 1 in table:
                ans = max(ans, table[i] + table[i + 1])

        return ans if ans != float('-inf') else 0

