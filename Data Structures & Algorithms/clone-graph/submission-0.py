"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.cache =  {}
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node.val in self.cache:
            return self.cache[node.val]

        new_node = Node(node.val)
        self.cache[node.val] = new_node

        for n in node.neighbors:
            child = self.cloneGraph(n)
            if child:
                new_node.neighbors.append(child)

        return new_node
        