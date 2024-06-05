class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = [0] * 26
        for i in words[0]:
            ans[ord(i) - ord('a')] += 1
        
        for i in words[1:]:
            tmp = [0] * 26
            for j in i:
                tmp[ord(j) - ord('a')] += 1
            for i in range(26):
                ans[i] = min(ans[i], tmp[i])
                
        res = []
        for i in range(26):
            for j in range(ans[i]):
                res += chr(i + ord('a'))
        return res