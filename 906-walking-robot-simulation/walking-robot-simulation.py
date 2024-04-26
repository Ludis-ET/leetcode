from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        gps = 0
        max_distance = 0
        obstacle_set = set((i, j) for i, j in obstacles)
        
        for command in commands:
            if command == -1:
                gps = (gps + 1) % 4
            elif command == -2:
                gps = (gps - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = directions[gps]
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance
