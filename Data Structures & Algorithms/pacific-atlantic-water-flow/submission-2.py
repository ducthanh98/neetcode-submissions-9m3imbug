class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_r = len(heights)
        max_c = len(heights[0])
        
        pac, atl = set(), set()

        def bfs(init):
            visited = set(init)

            q = deque(init)

            while q:
                r,c = q.popleft()
                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr,nc = r + dr, c + dc

                    if 0 <= nr < max_r and 0<= nc < max_c and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited 
        tmp = []
        for c in range(max_c):
            tmp.append((0, c))              # hàng trên
        for r in range(max_r):
            tmp.append((r, 0))              # cột trái
        pac = bfs(tmp)

        tmp = []
        for c in range(max_c):
            tmp.append((max_r - 1, c))      # hàng dưới
        for r in range(max_r):
            tmp.append((r, max_c - 1))      # cột phải
        atl = bfs(tmp)
        return [[r,c] for r,c in pac & atl]

                
