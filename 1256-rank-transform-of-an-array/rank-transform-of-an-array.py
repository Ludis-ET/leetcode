class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table, rank = defaultdict(int), 1
        for val in sorted(arr):
            if val not in table:
                table[val] = rank
                rank += 1
                
        for i, val in enumerate(arr):
            arr[i] = table[val]
        
        return arr