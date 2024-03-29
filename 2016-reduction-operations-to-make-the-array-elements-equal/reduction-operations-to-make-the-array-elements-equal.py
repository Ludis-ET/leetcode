class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        unq = sorted(count.keys(), reverse=True)
        op = 0
        prev = 0
        for num in unq[:-1]:
            op += count[num] + prev
            prev += count[num]
        return op