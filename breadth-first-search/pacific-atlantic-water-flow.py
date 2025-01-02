class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_reach = set()
        atlantic_reach = set()
        def dfs(r,c, reach):
            reach.add((r,c))
            directions= [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if (nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c] and (nr,nc) not in reach):
                    dfs(nr, nc, reach)

        for r in range(rows):
            dfs(r, 0, pacific_reach)
            dfs(r, cols-1, atlantic_reach)
        for c in range(cols):
            dfs(0,c, pacific_reach)
            dfs(rows-1, c, atlantic_reach)
        res = list(pacific_reach & atlantic_reach)
        return res