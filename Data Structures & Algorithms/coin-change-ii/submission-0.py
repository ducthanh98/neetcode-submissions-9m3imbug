import sys
sys.setrecursionlimit(10000)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(total, idx):
            if idx >= len(coins) or total > amount:
                return 0

            if total == amount:
                return 1

            if (total,idx) in dp:
                return dp[(total,idx)]

            tmp = dfs(total + coins[idx], idx) + dfs(total, idx + 1)

            dp[(total,idx)] = tmp
            return tmp




        return dfs(0, 0)