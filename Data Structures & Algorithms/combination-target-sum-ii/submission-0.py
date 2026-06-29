class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(remain: int, arr: List[int], candidates: List[int], idx: int):
            if remain == 0:
                res.append(arr.copy())
                return

            for i in range(idx, len(candidates)):
                if remain - candidates[i] < 0:
                    break
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                arr.append(candidates[i])
                backtrack(remain - candidates[i], arr, candidates, i + 1)
                arr.pop()
        backtrack(target, [], candidates, 0)
        return res

