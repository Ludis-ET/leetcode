class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = defaultdict(int)
        for i in s1.split():
            table[i] += 1
        for i in s2.split():
            table[i] += 1
        return [i for i, j in table.items() if j == 1]