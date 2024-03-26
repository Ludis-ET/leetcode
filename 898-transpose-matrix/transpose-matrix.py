class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for a, b in enumerate(matrix):
            for c, d in enumerate(b):
                transpose[c][a] = matrix[a][c]
        return transpose
