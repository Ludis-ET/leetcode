class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        but = {
            "2" : 'abc',
            "3" : 'def',
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }
        ans = []
        def back(i, cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return 
            for c in but[digits[i]]:
                back(i + 1, cur + c)
        back(0, "")
        return ans if digits else []