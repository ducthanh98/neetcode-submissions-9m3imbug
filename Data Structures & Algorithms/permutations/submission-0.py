class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []
        def backtrack(visited: List[bool], arr : List[int]):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for i in range(0, len(nums)):
                if not visited[i]:
                    arr.append(nums[i])
                    visited[i] = True
                    backtrack(visited, arr)
                    arr.pop()
                    visited[i] = False
        backtrack(visited, [])
        return res
            

