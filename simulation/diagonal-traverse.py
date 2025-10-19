class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []

        rows, cols = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        up = True

        for _ in range(rows * cols):
            result.append(mat[r][c])

            if up:
                if c == cols - 1:
                    r += 1
                    up = False
                elif r == 0:
                    c += 1
                    up = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1:
                    c += 1
                    up = True
                elif c == 0:
                    r += 1
                    up = True
                else:
                    r += 1
                    c -= 1

        return result