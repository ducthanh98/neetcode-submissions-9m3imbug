class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for _ in range(len(edges) + 1)]
        res = []

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u] 
        
        def union(u,v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False

            if rank[root_u]  < rank[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u

            if rank[root_u] == rank[root_v]:
                rank[root_u] +=1

            return True

        for (u,v) in edges:
            if not union(u,v):
                return [u,v ]

        return res

            