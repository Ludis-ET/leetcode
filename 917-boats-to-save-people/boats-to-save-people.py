class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        first, second = 0, len(people) - 1
        while first <= second:
            if people[first] + people[second] <= limit:
                first += 1
                second -= 1
            else:
                second -=1
            boat += 1
        return boat