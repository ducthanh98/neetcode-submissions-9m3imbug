class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, tmp):
            res.append(tmp.copy())
            for n in range(i , len(nums)):
                tmp.append(nums[n])
                backtrack(n + 1 , tmp)
                tmp.pop()

        backtrack(0,[])

        return res


