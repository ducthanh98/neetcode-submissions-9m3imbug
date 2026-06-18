class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            dist = -(p[0]**2 + p[1]**2)

            heapq.heappush(max_heap, (dist, [p[0], p[1]]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for dist,point in max_heap]
        