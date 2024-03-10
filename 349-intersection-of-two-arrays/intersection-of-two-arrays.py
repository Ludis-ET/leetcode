class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums1:
            hashmap[num] += 1
        ans = set()
        for num in nums2:
            if hashmap[num] > 0:
                ans.add(num)
        return ans
