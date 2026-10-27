class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        cache = {}

        def dp(total):
            if total == n:
                return 1
            if total >n :
                return 0
            key = n - total
            if key in cache:
                return cache[key]
            
            tmp = dp(total + 1) + dp(total + 2)
            cache[n - total] = tmp
            return tmp
        
        return dp(0)
