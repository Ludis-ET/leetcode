class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        table = defaultdict(list)
        
        for i, num in enumerate(nums):
            for j in table[num]:
                if (i * j) % k == 0:
                    count += 1
            table[num].append(i)
        
        return count
