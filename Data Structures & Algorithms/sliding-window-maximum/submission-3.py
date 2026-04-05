class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        q = deque()

        res = []
        for r in range(len(nums)):
            
            if q and q[0] == r - k:
                q.popleft()

            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            
            if r - l + 1 == k :
                res.append(nums[q[0]])
                l += 1
        return res