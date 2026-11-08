class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}

        def dfs(day, buying ):
            if day >= len(prices):
                return 0

            if (day,buying) in dp:
                return dp[(day,buying)]

            cooldown = dfs(day +1, buying)

            if buying:
                buy_profit = dfs(day +1, False) - prices[day]
                dp[(day,buying)] = max(buy_profit, cooldown)
            else:
                sell_profit = dfs(day + 2 , True) + prices[day]
                dp[(day,buying)] = max(sell_profit, cooldown)

            return dp[(day,buying)]

        return dfs(0, True)