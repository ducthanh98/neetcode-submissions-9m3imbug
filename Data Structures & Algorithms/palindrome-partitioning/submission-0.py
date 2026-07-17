class Solution:
    def is_palindrome(self, s: list[str]):
        i,j = 0,len(s) - 1
        while i < j:

            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def backtrack( start: int ,current_result: list[str] ):
            if start == len(s):
                res.append(current_result.copy())
                return

            for end in range(start +1, len(s) + 1):
                piece = s[start:end]
                if self.is_palindrome(piece):
                    current_result.append(piece)
                    backtrack(end, current_result)
                    current_result.pop()

            
        backtrack(0, [])
        return res