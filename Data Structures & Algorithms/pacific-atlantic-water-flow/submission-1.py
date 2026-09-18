class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_r = len(heights)
        max_c = len(heights[0])
        
        pac, atl = set(), set()

        def dfs (r,c,visited):
            visited.add((r,c))

            for dr,dc in ((0,1), (0,-1), (-1,0),(1,0)):
                nr,nc = r + dr, c + dc

                if 0 <= nr <max_r and 0 <= nc < max_c and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,visited)

        for c in range(max_c):
            dfs(0, c, pac)
            dfs(max_r - 1, c, atl)

        for r in range(max_r):
            dfs(r,0, pac)
            dfs(r, max_c -1, atl)
        return [[r,c] for r,c in pac& atl]
                
