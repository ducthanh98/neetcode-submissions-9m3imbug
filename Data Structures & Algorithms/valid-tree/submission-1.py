class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Trick lọc cửa miệng
        if len(edges) != n - 1:
            return False

        # 2. Xây dựng đồ thị vô hướng (build sẵn n đỉnh cho sạch)
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)  # <--- Bắt buộc phải có chiều ngược lại

        # Dùng Set thay vì Dict cho visited để thao tác dễ hơn
        visited = set()

        # 3. Hàm DFS giờ chỉ làm nhiệm vụ "loang" vết dầu
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        # 4. GỌI HÀM TỪ ĐỈNH 0!
        dfs(0)

        # 5. Nếu từ 0 mà loang ra được hết n đỉnh -> Liên thông -> Hợp lệ
        return len(visited) == n