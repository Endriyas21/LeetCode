class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        for i in range(rows):
            for j in range(i,rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # for i in range(rows):
        #     matrix[i].reverse()
        for i in range(rows):
            for j in range(rows//2):
                matrix[i][j], matrix[i][rows-1-j] = matrix[i][rows-1-j], matrix[i][j]
        