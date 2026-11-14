class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        adj = ((0,1),(0,-1),(1,0),(-1,0))

        m,n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(r,c):
            if dp[r][c] > 0:
                return dp[r][c]
            path = 1

            for (i,j) in adj:
                nr = r +i
                nc = c + j
                if 0 <= nr < m and 0 <= nc < n and matrix[r][c] < matrix[nr][nc]:
                    tmp = 1 + dfs(nr,nc)
                    if tmp > path:
                        path = tmp

            dp[r][c] = path
            return path
        ans = 0 

        for i in range(m):
            for j in range(n):
                ans  = max(ans, dfs(i,j))



        return ans
