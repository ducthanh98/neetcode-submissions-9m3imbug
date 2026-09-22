class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        maxr = len(grid)
        maxc = len(grid[0])


        def dfs(r,c, maxr, maxc):
            if r <0 or c <0 or r >= maxr or c >= maxc or grid[r][c] == "-" or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "-"
            for i,j in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(r +i, c + j, maxr, maxc)



        count = 0
        for r in range(maxr):
            for c in range(maxc):
                if grid[r][c] == "-" or grid[r][c] == "0":
                    continue
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c, maxr,maxc)
        return count
