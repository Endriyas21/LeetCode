class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()
        fresh = 0
        def addRows(r, c):
            nonlocal fresh
            if (r in range(rows) and c in range(cols) and (r,c) not in seen and grid[r][c] == 1):
                seen.add((r,c))
                q.append((r,c))
                fresh-=1
                grid[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 2):
                    q.append((r,c))
                    seen.add((r,c))
                elif (grid[r][c] == 1):
                    fresh+=1
        time = 0
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                addRows(r+1,c)
                addRows(r-1,c)
                addRows(r,c+1)
                addRows(r,c-1)
            time+=1
        return time if not fresh else -1
                
