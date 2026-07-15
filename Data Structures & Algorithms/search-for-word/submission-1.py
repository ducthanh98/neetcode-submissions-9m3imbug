class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_row, len_col = len(board), len(board[0])

        def backtrack(idx: int, r: int, c: int):
            if idx == len(word):
                return True

            if r >= len_row or c >= len_col or r < 0  or c < 0 or board[r][c] != word[idx] : 
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            found =(backtrack(idx + 1 , r + 1, c ) or 
                    backtrack(idx + 1 , r, c  + 1 ) or
                    backtrack(idx + 1 , r - 1, c ) or  
                    backtrack(idx + 1 , r , c - 1 ))
            if found:
                return True
            
            board[r][c] = tmp
            return False
        
        for r in range(len_row):
            for c in range(len_col):
                if board[r][c] == word[0]:
                    res = backtrack(0, r, c)
                    if res:
                        return True
        return False
