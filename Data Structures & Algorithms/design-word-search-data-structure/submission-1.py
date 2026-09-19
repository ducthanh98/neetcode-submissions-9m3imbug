class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            cur = node
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # Rẽ nhánh qua tất cả con hiện có
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.is_end_of_word

        return dfs(self.root, 0)