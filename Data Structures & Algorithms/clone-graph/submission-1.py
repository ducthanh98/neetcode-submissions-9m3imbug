class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary lưu trữ node cũ -> node mới
        # Khởi tạo cục bộ trong hàm để an toàn với mọi test case
        visited = {}
        
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            # Tạo node clone và lưu vào dictionary NGAY LẬP TỨC
            # để tránh lặp vô tận (infinite loop) nếu có chu trình
            clone = Node(curr_node.val)
            visited[curr_node] = clone
            
            # Clone các node hàng xóm
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)