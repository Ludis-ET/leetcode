class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)

        for i in nums: table[i] += 1

        ans = [[x, y] for x, y in table.items()]
        ans.sort(key=lambda x:x[1], reverse=True)
        
        return [b[0] for a, b in enumerate(ans) if a < k]