class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        dict = {node: float('inf') for node in range(1,n + 1)}

        dict[k] = 0
        pq = [(0,k)]

        while pq:
            d,u = heapq.heappop(pq)
            if d > dict[u]:
                continue

            for v,w in graph[u]:
                if dict[u] + w < dict[v]:
                    dict[v] = dict[u] + w 
                    heapq.heappush(pq, (dict[v],v))

        max_time = max(dict.values())
        return max_time if max_time < float('inf') else -1 
