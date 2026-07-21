class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []

        current_result = [["."] * n for _ in range(n)]

        cols = [False] * n
        diag1 = [False]*2*n
        diag2 = [False]*2*n

        def backtrack(r):
            if r == n:

                results.append(["".join(row) for row in current_result])
                return
            
            for c in range(n):
                idx1 = r - c + n 
                idx2 = r + c 
                if cols[c] or diag1[idx1] or diag2[idx2] :
                    continue
                cols[c] = diag1[idx1] = diag2[idx2] = True
                current_result[r][c] = "Q"
                backtrack(r+ 1)
                current_result[r][c] = "."
                cols[c] = diag1[idx1] = diag2[idx2]  = False

        backtrack(0)

        return results