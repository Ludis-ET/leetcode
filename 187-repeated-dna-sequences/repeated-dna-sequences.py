class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table, ans = set(), set()
        for l in range(len(s) - 9):
            c = s[l: l + 10]
            if c in table:
                ans.add(c)
            table.add(c)
        return ans