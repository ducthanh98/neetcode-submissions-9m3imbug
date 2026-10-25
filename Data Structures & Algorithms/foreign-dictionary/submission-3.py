class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for w in words for char in w }
        in_degree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_length = min(len(w1), len(w2))
            if len(w2) < len(w1) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                c1,c2 = w1[j], w2[j]

                if c1 != c2:
                    if not c2 in adj[c1]:
                        in_degree[c2] += 1 
                        adj[c1].add(c2)
                    break
        
        res = []
        q = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)

        while q:
            item = q.popleft()
            res.append(item)

            for c in adj[item]:
                in_degree[c] -= 1 
                if in_degree[c] == 0:
                    q.append(c)

        if len(res) < len(in_degree):
            return ""

        return "".join(res)
            

        


 