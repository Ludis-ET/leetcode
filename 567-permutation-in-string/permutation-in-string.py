class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table1 = defaultdict(int)
        for i in s1:
            table1[i] += 1
        
        def check(s2):
            table2 = defaultdict(int)
            for i in s2:
                table2[i] += 1
            return table1 == table2
        
        l, r = 0, len(s1)
        while r <= len(s2):
            if check(s2[l:r]):
                return True
            l += 1
            r += 1
        return False