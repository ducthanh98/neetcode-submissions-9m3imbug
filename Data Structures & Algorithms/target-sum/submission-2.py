class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        length = len(nums)

        def dp(idx, total):
            if idx == length and total == target:
                return 1 

            if idx >= length:
                return 0


            if (idx,total) in cache:
                return cache[(idx,total)]
            cache[(idx,total)] = dp(idx + 1, total + nums[idx]) + dp(idx + 1, total - nums[idx])

            return cache[(idx,total)]

        return dp(0,0)

