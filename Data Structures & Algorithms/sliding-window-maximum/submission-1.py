class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        state = {}
        l = 0

        res = []
        for r in range(len(nums)):
           
            state[nums[r]] = state.get(nums[r], 0) + 1
            if r - l + 1 == k :

                max_val = float('-inf')
                for key,v in state.items():
                    if key > max_val and v > 0:
                        max_val = key
                
                res.append(max_val)

                state[nums[l]] -= 1
                l += 1
        return res