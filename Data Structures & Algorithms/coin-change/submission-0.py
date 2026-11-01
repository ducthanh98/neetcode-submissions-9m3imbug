class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = len(coins)
        cache = {}


        def dp(remain):
            if remain ==0:
                return 0
            if remain < 0 :
                return float('inf')

            if remain in cache:
                return cache[remain]
            min_coins = float('inf')
            for coin in coins:
                tmp = dp(remain - coin)
                min_coins = min(tmp + 1 , min_coins)
            cache[remain] = min_coins
            return cache[remain]            

        ans = dp(amount)
        print(cache)

        return -1 if ans == float('inf')  else ans
