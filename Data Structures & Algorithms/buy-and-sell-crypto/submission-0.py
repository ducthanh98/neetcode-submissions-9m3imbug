class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 99999
        res = 0
        for price in prices:
            if min_price > price:
                min_price = price
            benefit = price - min_price
            if benefit > res :
                res = benefit

        return res