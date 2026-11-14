class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        cache = {}
        def dp(i, j):
            if j == n :
                return 1
            if i == m :
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            cache[(i,j)]  = dp(i+1, j) + ( dp(i+1, j+1) if s[i] == t[j] else 0  )
            return cache[(i,j)]

        return dp(0,0)