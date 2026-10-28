class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            if len(arr) == 1:
                return arr[0]

            prev2 = 0
            prev1 = arr[0]

            for i in range(1, len(arr)):
                cur = max(prev1, prev2 + arr[i])
                prev2 = prev1
                prev1 = cur
            
            return prev1  # <-- THIẾU DÒNG NÀY NÈ!

        return max(dp(nums[:-1]), dp(nums[1:]))