class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Chuyển sang Set để tra cứu O(1)
        if endWord not in wordSet:
            return 0

        visited = {}
        visited[beginWord] = True

        q = deque()
        q.append([beginWord, 1 ])

        while q:
            w,cnt = q.popleft()
            if w == endWord:
                return cnt

            for i in range(len(w)):
                for j in range(26):
                    new_char = chr(97 + j)
                    new_word = w[:i] + new_char + w[i+1:]

                    if not new_word in visited and new_word in wordSet and not new_word in visited:
                        visited[new_word] = True 
                        q.append([new_word, cnt + 1 ])
        
        return 0
                


        



        