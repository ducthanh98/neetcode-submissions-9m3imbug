from typing import Counter


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:

    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, word: str):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end_of_word = True

    def dfs(self, r,c, max_r, max_c , tmp, outputs, cur,board):
        if r < 0 or c < 0 or r >= max_r or c >= max_c or board[r][c] == "-":
            return
        key = board[r][c]


        if key in cur.children:

            board[r][c] = "-"

            for i,j in ((0,1),(0,-1), (-1,0), (1,0)):
                tmp.append(key)
                next = cur.children[key]
                if not next:
                    continue
                if next.is_end_of_word:
                    next.is_end_of_word = False
                    outputs.append(tmp[:])
                self.dfs(r + i, c +j, max_r, max_c, tmp, outputs, next,  board)
                tmp.pop()
            board[r][c] = key



    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        for w in words:
            self.buildTrie(w)


        max_r = len(board)
        max_c = len(board[0])
        outputs = []
        tmp = []

        for r in range(max_r):
            for c in range(max_c):
                self.dfs(r,c, max_r, max_c, tmp, outputs, self.root,board)

        return ["".join(output) for output in outputs]




