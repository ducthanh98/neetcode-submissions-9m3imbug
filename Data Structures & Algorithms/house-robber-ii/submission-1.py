class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Hàm giải House Robber tuyến tính (House Robber I)
        def rob_linear(arr):
            if not arr: return 0
            if len(arr) == 1: return arr[0]
            
            prev2 = 0
            prev1 = arr[0]
            for i in range(1, len(arr)):
                current = max(prev1, prev2 + arr[i])
                prev2 = prev1
                prev1 = current
            return prev1

        # Vòng tròn: Lấy max giữa (Bỏ nhà cuối) và (Bỏ nhà đầu)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))