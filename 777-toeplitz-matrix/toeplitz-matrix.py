class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for a in range(1, len(matrix)):
            for b in range(1, len(matrix[a])):
                if matrix[a][b] != matrix[a-1][b-1]:
                    return False
        return True

        