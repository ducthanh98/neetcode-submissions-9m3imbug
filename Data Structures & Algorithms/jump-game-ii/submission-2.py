class Solution:
    def jump(self,nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        # Chỉ duyệt đến n - 2 vì khi chạm hoặc vượt n - 1 là đã tới đích
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps