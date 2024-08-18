class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, cur, count = [], [], Counter(nums)
        def back():
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return 
            for k, v in count.items():
                if v > 0:
                    cur.append(k)
                    count[k] -= 1
                    back()
                    count[k] += 1
                    cur.pop()
        back()
        return ans