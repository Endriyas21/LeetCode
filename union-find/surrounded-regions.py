class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def capture(r, c):
            if r in range(rows) and c in range(cols) and board[r][c] == "O":
                board[r][c] = "T"
                capture(r, c - 1)
                capture(r, c + 1)
                capture(r + 1, c)
                capture(r - 1, c)
        
        # Step 1: Capture unsurrounded regions (connected to boundary)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)
        
        # Step 2: Flip all remaining "O" to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Step 3: Restore all "T" to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"