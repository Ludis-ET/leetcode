class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = defaultdict(int)
        for a, b in enumerate(nums):
            if table[b] == 0: table[b] = a + 1
            else:
                if abs(table[b] - (a+1)) <= k: return True
                else: table[b] = a + 1
        return False
            