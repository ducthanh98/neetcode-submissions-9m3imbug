class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        maxr = len(grid)
        maxc = len(grid[0])

        def dfs(r,c ):
            if r < 0 or c < 0 or r >= maxr or c >= maxc or grid[r][c] == 0 or grid[r][c] == "-":
                return 0
            count = 1
            grid[r][c] = "-"
            for i,j in ((0,1),(0,-1),(1,0),(-1,0)):
                count += dfs(r +i, c + j)


            return count


        for r in range(maxr):
            for c in range(maxc):
                if grid[r][c] == 1:
                    count = dfs(r, c )
                    if count > max_area:
                        max_area = count

        return max_area