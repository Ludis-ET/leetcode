class Solution(object):
    def similarPairs(self, words):
        seen = {}
        res = 0
        for word in words:
            key = tuple(set(word))
            if key in seen:
                res += seen[key]
                seen[key] +=1
            else:
                seen[key] = 1
        return res     