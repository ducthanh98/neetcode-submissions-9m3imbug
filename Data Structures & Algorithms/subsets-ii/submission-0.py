class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(arr: List[int], idx: int):
            res.append(arr.copy())
            print(nums, idx)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtrack(arr, i + 1)
                arr.pop()

        backtrack([], 0)
        return res        