class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums: List[int], total: int, arr: List[int] , target: int, idx: int):
            if total == target:
                res.append(arr.copy())                
                return
            elif total > target:
                return

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                total = total + nums[i]
                backtrack(nums, total, arr, target, i)
                arr.pop()

                total = total - nums[i]

        backtrack(nums, 0, [], target,0)
        return res

            