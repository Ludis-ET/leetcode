class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        table = defaultdict(int)
        result = []
        
        for num in arr1:
            table[num] += 1
        
        for num in arr2:
            result.extend([num] * table[num])
            del table[num]
        
        for num in sorted(table.keys()):
            result.extend([num] * table[num])
        
        return result