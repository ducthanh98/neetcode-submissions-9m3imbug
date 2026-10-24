class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        lr,lc = len(grid) - 1, len(grid[0]) - 1
        adj = ((0,1),(1,0),(-1,0),(0,-1))
        q =[(grid[0][0],0,0)]
        res = -1


        visited = set()

        while q:
            v, x,y = heapq.heappop(q)

            if (x,y) in visited:
                continue

            visited.add((x,y))
            if v > res:
                res = v
            if x == lr and y == lc:
                return res

            for t1,t2 in adj:
                nr,nc = x + t1, y + t2
                if 0 <= nr <= lr and 0 <= nc <= lc and (nr,nc) not in visited:
                    heapq.heappush(q,(grid[nr][nc], nr ,nc))

        return -1 
