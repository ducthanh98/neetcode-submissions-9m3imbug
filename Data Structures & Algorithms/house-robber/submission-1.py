class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        max_res = 0
        cache = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            if i in cache:
                return cache[i]
            sub = max(dp(i + 2), dp(i+3))
            cache[i] = sub + nums[i]
            return cache[i]
        return max(dp(0), dp(1))
