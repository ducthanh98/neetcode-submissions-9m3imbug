class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for n in word:
            if not n in cur.children:
                cur.children[n] = TrieNode()

            cur = cur.children[n]
        cur.is_end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        
        for n in word:
            if n in cur.children:
                cur = cur.children[n]
            else:
                return False
        return cur.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for n in prefix:
            if not n in cur.children:
                return False
            cur = cur.children[n]
        return True
        
        