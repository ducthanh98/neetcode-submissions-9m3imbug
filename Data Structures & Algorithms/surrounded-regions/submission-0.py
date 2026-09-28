class Solution:
    def solve(self, board: List[List[str]]) -> None:
        maxr = len(board)
        maxc = len(board[0])
        q = deque()

        for r in range(maxr):
            if board[r][0] == 'O':
                    q.append((r,0))
                    board[r][0] = 'T'
            if board[r][maxc - 1] == 'O':
                q.append((r,maxc - 1))
                board[r][maxc - 1 ] = 'T'

            
        for c in range(maxc):
                if board[0][c] == 'O':
                    q.append((0,c))
                    board[0][c] = 'T'

                if board[maxr - 1 ][c] == 'O':
                    q.append((maxr - 1 ,c))
                    board[maxr - 1 ][c] = 'T'


        while q:
            r,c = q.popleft()

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r + dr, c + dc

                if 0 <= nr < maxr and 0 <= nc < maxc and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    q.append((nr,nc))

        for r in range( maxr):
            for c in range(maxc):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
