class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cur, hp = 0, []
        for dur, lst in courses:
            heapq.heappush(hp, -dur)
            cur += dur
            if cur > lst:
                cur -= -heapq.heappop(hp)
        return len(hp)