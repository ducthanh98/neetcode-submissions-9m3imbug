class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited_node = {}

        for a,b in edges:
            if a in adj:
                adj[a].append(b)
            else :
                adj[a] = [b]

            if b in adj:
                adj[b].append(a)
            else :
                adj[b] = [a]
        count = 0
        def dfs(n):
            if n in visited_node:
                return
            
            visited_node[n] = True
            if n not in adj:
                return

            for v in adj[n]:

                dfs(v)

        for i in range(n):
            if not i in visited_node:
                dfs(i)
                count += 1 

        return count 