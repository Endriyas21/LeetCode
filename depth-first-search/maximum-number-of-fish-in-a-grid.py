class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFish = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            temp_fish = grid[r][c]
            q = deque()
            q.append((r,c))
            seen.add((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    newRow, newCol = r+dr, c+dc
                    if (newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] != 0):
                        temp_fish+=grid[newRow][newCol]
                        seen.add((newRow,newCol))
                        q.append((newRow, newCol))
                return temp_fish

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] != 0:
                    maxFish = max(maxFish, bfs(r,c))
        return maxFish