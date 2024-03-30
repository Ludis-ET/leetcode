class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        a, b = len(s), len(goal)
        if a != b:return False
        if s == goal:
            ss = set()
            for c in s:
                if c in ss:
                    return True
                ss.add(c)
            return False
        
        arr = []
        for i in range(a):
            if s[i] != goal[i]:
                arr.append(i)
        
        if len(arr) != 2:
            return False
        
        return s[arr[0]] == goal[arr[1]] and s[arr[1]] == goal[arr[0]]
