class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        res  = []
        def backtrack(count:int, idx: int , current_result: str):
            if count == len(digits):
                res.append(current_result)
                return

            for v in mapping[digits[idx]]:
                current_result += v
                backtrack(count + 1, idx + 1, current_result)
                current_result = current_result[:-1]


        backtrack(0, 0 , "")
        return res
        