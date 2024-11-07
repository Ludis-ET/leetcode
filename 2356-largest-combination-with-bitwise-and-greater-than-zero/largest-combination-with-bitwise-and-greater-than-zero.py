class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        table = defaultdict(int)
        for num in candidates:
            for i in range(num.bit_length()):
                if num & 1 << i != 0:
                    table[i] += 1
        return max(table.values())