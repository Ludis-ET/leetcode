class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []
        for a in candies:
            ans.append(True if a + extraCandies >= m else False)
        return ans