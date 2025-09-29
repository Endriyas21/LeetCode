class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        q = deque()

        # Step 1: Add border O's to queue
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][cols - 1] == "O":
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))

        # Step 2: BFS from border 'O's and mark them as 'E' (escape)
        while q:
            r, c = q.popleft()
            if board[r][c] != "O":
                continue
            board[r][c] = "E"  # Temporarily mark as escape
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    q.append((nr, nc))

        # Step 3: Flip all 'O' to 'X' (surrounded), and 'E' back to 'O' (safe)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"