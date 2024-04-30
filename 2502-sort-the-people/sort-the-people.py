class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        table = []

        for i in range(len(heights)):
            table.append([names[i], heights[i]])

        table.sort(key=lambda x: x[1], reverse=True)
        return [f for f, s in table]