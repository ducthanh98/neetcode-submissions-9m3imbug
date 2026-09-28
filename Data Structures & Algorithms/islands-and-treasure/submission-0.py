INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        maxr = len(grid)
        maxc = len(grid[0])

        q = deque()

        for r in range(maxr):
            for c in range(maxc):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r + dr, c + dc
                if 0 <= nr < maxr and 0 <= nc < maxc and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1 
                    q.append((nr,nc))

