class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = sorted(nums)
        table = defaultdict(int)
        ans = []
        for i, v in enumerate(tmp):
            if tmp[i] not in table:
                table[v] = i
        
        for i, v in enumerate(nums):
            ans.append(table[v])
        return ans