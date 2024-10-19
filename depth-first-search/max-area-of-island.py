class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols  = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                direction = [[1,0],[-1,0], [0,1],[0,-1]]
                for dr, dc in direction:
                    r,c = dr+row, dc+col
                    if (r in range(rows) and c in range(cols)) and grid[r][c] == 1 and (r,c) not in visited:
                        area+=1
                        q.append((r,c))
                        visited.add((r,c))
            return area
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea


