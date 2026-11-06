class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m) ]


        def dp(i,j):
            if i == m -1 and j == n - 1 :
                return 1

            if i >= m or j >= n:
                return 0

            if cache[i][j]:
                return cache[i][j]

            right = dp(i+1, j)
            bottom = dp(i, j+1)
            cache[i][j] = right + bottom
            return cache[i][j]

        return dp(0,0)