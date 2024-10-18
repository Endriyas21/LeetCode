class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island=0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0], [0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = r+dr, c+ dc

                    if (r in range(rows) and c in range(cols)) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island 