from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Bước 1: Xây dựng đồ thị
        graph = defaultdict(list)
        res = []
        
        for src,dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        def dfs(airport):
            while graph[airpot]:
                next_air 

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Bước 1: Xây dựng đồ thị
        graph = defaultdict(list)
        
        # Sắp xếp vé theo thứ tự từ điển giảm dần
        # để khi dùng .pop() sẽ lấy được phần tử nhỏ nhất trước với O(1)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        route = []
        
        # Bước 2: DFS Hierholzer
        def dfs(airport):
            while graph[airport]:
                # Lấy sân bay kế tiếp có thứ tự từ điển nhỏ nhất
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # Khi hết đường đi tiếp (gặp ngõ cụt), ghi nhận sân bay này
            route.append(airport)
            
        dfs("JFK")        
        print()

        return route[::-1]
    