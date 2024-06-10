class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 < stack[-1]:
                l = stack[-1]
                if l < -i:
                    stack.pop()
                    continue
                elif l == -i:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack