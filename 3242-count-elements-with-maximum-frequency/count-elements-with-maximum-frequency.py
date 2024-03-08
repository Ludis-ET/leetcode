class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for a in nums:
            hashmap[a] += 1
        m = max(hashmap.values())
        ans = 0
        for key, value in hashmap.items():
            if value == m:
                ans += value
        return ans