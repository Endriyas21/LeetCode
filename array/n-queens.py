class Solution:
    def solveNQueens(self, n: int):
        def is_safe(row, col):
            return not cols[col] and not diag[row - col + n - 1] and not anti_diag[row + col]

        def place_queens(row):
            if row == n:
                # Convert board to desired format and add to results
                board = []
                for r in range(n):
                    line = ""
                    for c in range(n):
                        line += 'Q' if columns[r] == c else '.'
                    board.append(line)
                results.append(board)
                return

            for col in range(n):
                if is_safe(row, col):
                    # Place the queen
                    columns[row] = col
                    cols[col] = diag[row - col + n - 1] = anti_diag[row + col] = True

                    # Move to the next row
                    place_queens(row + 1)

                    # Backtrack
                    cols[col] = diag[row - col + n - 1] = anti_diag[row + col] = False

        # Initialize the structures
        results = []
        columns = [-1] * n
        cols = [False] * n
        diag = [False] * (2 * n - 1)
        anti_diag = [False] * (2 * n - 1)

        # Start placing queens from the first row
        place_queens(0)
        return results

# Example usage:
# solution = Solution()
# print(solution.solveNQueens(4))