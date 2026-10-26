class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. Xây dựng danh sách kề
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        # 2. Mảng lưu chi phí tốt nhất đến mỗi đỉnh
        prices = [float('inf')] * n
        prices[src] = 0
        
        # 3. Chạy tối đa k + 1 lần (mỗi lần là 1 lớp/chặng bay)
        for _ in range(k + 1):
            temp_prices = prices.copy()
            
            # Thay vì duyệt qua từng flights, ta duyệt qua từng đỉnh u có trong đồ thị
            for u in range(n):
                if prices[u] == float('inf'):
                    continue
                
                # Duyệt qua các hàng xóm v của u thông qua adj
                for v, w in adj[u]:
                    if prices[u] + w < temp_prices[v]:
                        temp_prices[v] = prices[u] + w
                        
            prices = temp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1