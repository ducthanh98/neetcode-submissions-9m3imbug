# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        result = ""
        if not root:
            return "#"
        
        q.append(root)

        while q:
            count  = len(q)

            for i in range(count):
                node = q.popleft()
                v = node.val if node else "#"
                if result == "":
                    result = str(v)
                else:
                    result += "," + str(v)

                if node:
                    q.append(node.left)
                    q.append(node.right)
        return result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        if arr[0] == "#":
            return None
        q = deque()
        i = 0
        root = TreeNode(arr[i],None,None)
        q.append(root)
        i = i + 1 

        while q and i < len(arr):
            node = q.popleft()

            if arr[i] != "#":
                left_node = TreeNode(arr[i],None,None)
                q.append(left_node)
                node.left = left_node
            i += 1
            
            if arr[i] != "#":
                right_node = TreeNode(arr[i],None,None)
                node.right = right_node
                q.append(right_node)
            i += 1    
        return root
