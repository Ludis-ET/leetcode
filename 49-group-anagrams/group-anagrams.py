class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for a in strs:
            count = [0]*26
            for b in a:
                count[ord(b) - ord('a')] += 1
            ans[tuple(count)].append(a)
        return ans.values()