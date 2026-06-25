class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        length = len(nums)
        path = []
        def backtrack(idx):
            if idx >= length:
                return
            
            path.append(nums[idx])
            res.append(path.copy())

            backtrack(idx + 1 )

            path.pop()
            backtrack(idx+1)

        backtrack(0)
        return res


