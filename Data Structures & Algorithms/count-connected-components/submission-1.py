class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [[0 for _ in range(n)] for _ in range(n)]
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
        def dfs(n, can_count):
            nonlocal count
            if n in visited_node:
                return
            if can_count:
                count += 1 
            
            visited_node[n] = True
            if n not in adj:
                return

            for v in adj[n]:
                if visited[n][v] == 1 or visited[v][n] == 1 :
                    continue
                visited[n][v] =  visited[v][n] = 1

                dfs(v,False)

        for i in range(n):
            dfs(i, True)

        return count 