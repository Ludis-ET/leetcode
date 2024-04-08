class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        count = 0          
        for a in nums:
            tar = k - a
            if tar >= 0 and table[tar] > 0:
                count += 1
                table[tar] -= 1
            else:
                table[a] += 1
        
        return count